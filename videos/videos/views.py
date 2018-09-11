from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, 


@view_config(route_name='videos', renderer='templates/videos/index.html', request_method='GET')
def list_videos(request):
    videos = request.db_video_analytics.videos.find({}, {'_id': False})
    return {'videos': videos}


@view_config(route_name='new_video', renderer='templates/videos/new.html', request_method='GET')
def add_video(request):
    return {}


@view_config(route_name='create_video', request_method='POST')
def add_video(request):
    name = request.params['name'].decode('utf-8')
    theme = request.params['theme'].decode('utf-8')
    request.db_video_analytics.insert_one({'name': name, 'theme': theme, 'thumbs_up':0, 'thumbs_down':0})
    return HTTPFound(request.route_url('videos'))

@view_config(route_name='thumbs_up', request_method='POST')
def add_video(request):
    video_name = request.matchdict.get('name', None)
    if video_name:
        video = request.db_video_analytics.videos.find_one({'name': name}, {'_id': False})
        if video:
            thumbs_up = video['thumbs_up'] + 1
            request.db_video_analytics.videos.update_one({'name': name}, {"$set":{"thumbs_up":thumbs_up}})
            
    return HTTPFound(request.route_url('videos'))




