import line

notify = line.line('token')

notify.send_message('hello world')
notify.send_photo(
    'https://p176.p0.n0.cdn.getcloudapp.com/items/2NuxGZrk/a.jpg')
notify.send_photo('a.png')
