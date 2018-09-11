def includeme(config):
    config.add_route('videos', '/videos/')
    config.add_route('new_video', '/videos/new/')
    config.add_route('create_video', '/videos/new/create/')
