class Template:
    def template_method(self, data):
        self.retrieve_obj()

        error = self.validate_output(data)

        if error:
            return error
        self.before_save_hook()
        self.query_to_save(data)
        self.after_save_hook()
        return self.response_status(code=None)

    def retrieve_obj(self):
        return self

    def validate_output(self, data):
        for value in data.values():
            if value is None:
                self.response_status(code=True)

    def query_to_save(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def response_status(self, code=None):
        if code:
            status_code = 400
            return {'status_code': status_code, 'status': 'Rejected'}

        status_code = 200
        return {'status_code': status_code, 'status': 'Updated'}

    def before_save_hook(self):
        print('Hook before making changes')

    def after_save_hook(self):
        print('Hook after changes were made')

