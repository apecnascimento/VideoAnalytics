from pyramid.view import view_config


@view_config(route_name='videos', renderer='templates/videos/index.html', request_method='GET')
def list_videos(request):
    videos = request.db_video_analytics.videos.find({}, {'_id': False})
    return {'videos': videos}