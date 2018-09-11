from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound 
from bson.son import SON


@view_config(route_name='videos', renderer='templates/videos/index.jinja2', request_method='GET')
def list_videos(request):
    videos = request.db_video_analytics.videos.find({}, {'_id': False})
    return {'videos': videos}


@view_config(route_name='new_video', renderer='templates/videos/new.jinja2', request_method='GET')
def new_video(request):
    return {}


@view_config(route_name='create_video', request_method='POST')
def create_video(request):
    name = request.params['name']
    theme = request.params['theme']
    request.db_video_analytics.videos.insert_one({'name': name, 'theme': theme, 'thumbs_up':0, 'thumbs_down':0})
    return HTTPFound(request.route_url('videos'))

@view_config(route_name='thumbs_up', request_method='POST')
def thumbs_up(request):
    video_name = request.matchdict.get('name', None)
    if video_name:
        video = request.db_video_analytics.videos.find_one({'name': video_name}, {'_id': False})
        if video:
            thumbs_up = video['thumbs_up'] + 1
            request.db_video_analytics.videos.update_one({'name': video_name}, {"$set":{"thumbs_up":thumbs_up}})
            
    return HTTPFound(request.route_url('videos'))


@view_config(route_name='thumbs_down', request_method='POST')
def thumbs_down(request):
    video_name = request.matchdict.get('name', None)
    if video_name:
        video = request.db_video_analytics.videos.find_one({'name': video_name}, {'_id': False})
        if video:
            thumbs_down = video['thumbs_down'] + 1
            request.db_video_analytics.videos.update_one({'name': video_name}, {"$set":{"thumbs_down":thumbs_down}})
            
    return HTTPFound(request.route_url('videos'))



@view_config(route_name='list_score', renderer='templates/videos/score.jinja2', request_method='GET')
def list_score(request):
    pipeline =     [
        {"$project": {"theme": 1, "score":{"$subtract":["$thumbs_up", { "$divide": ["$thumbs_down",2]}]} } },
        { "$group": { "_id": "$theme", "total_score": { "$sum" : "$score" }} },
        { "$sort": { "total_score": -1 } }        
    ]
    scores = request.db_video_analytics.videos.aggregate(pipeline)

    return {'scores': scores}
   

