import web


urls = (
    '/', 'index'
)


class index:
    def POST(self):
        data = None
        try:
            i = web.input()
            print i
            data = web.data()
            print data
            return
        except Exception, e:
            print e
        print data


if __name__ == "__main__":
    app = web.application(urls,
                          globals())
    app.run()
