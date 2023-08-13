def login_share(user_agent, ssid):
    header = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'User-Agent': config.user_agent,
        'Cookie': 'session_id=' + config.ssid
    }

    data = dict(url=url, password=password, token=config.token, zipflag=0)

    r = rq_fshare(url=config.file_dl_api_url, header=header, data=data)

    if r.status_code != 200:
        print("Skip this URL: {}, caused by: {}".format(url, error_info(r.status_code)))
        return ''

    json = request_to_json(r)
    return json['location']