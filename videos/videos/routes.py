def includeme(config):
    config.add_route('videos', '/')
    config.add_route('new_video', '/videos/new/')
    config.add_route('create_video', '/videos/new/create/')
    config.add_route('thumbs_up', '/videos/thumbsup/{name}/')
    config.add_route('thumbs_down', '/videos/thumbsdown/{name}/')
    config.add_route('list_score', '/videos/score/')