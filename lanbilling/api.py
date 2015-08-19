import logging
from lanbilling import lb
from lanbilling.exceptions import LBAPIError


class LANBilling(object):
    instance = None

    def __new__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(LANBilling, cls).__new__(cls)
        return cls.instance

    def __init__(self, manager='admin', password='', host='127.0.0.1', port=1502):
        port = int(port)

        self.logger = logging.getLogger(__name__)

        try:
            self.lbapi = lb.Client(host, port)
            self.lbapi.Login(login=manager, password=password)
        except Exception as e:
            self.logger.debug(e)
            raise LBAPIError(e)

    def __getattr__(self, method):
        return LBAPIMethod(self, method)

    def __call__(self, method, params):
        try:
            return self.lbapi.run(method, params)
        except RuntimeError, e:
            raise LBAPIError(e)

    def help(self, method_name):
        methods = self.lbapi.system_get_functors(None)
        if method_name is None:
            print 'Available methods:'
            print '\n'.join(method['name'] for method in methods)
            return
        for method in methods:
            if method['name'] == method_name:
                func = getattr(self.lbapi, method_name)
                func.__name__ = method['name']
                func.__doc__ = '\n\n'
                if 'descr' in method:
                    func.__doc__ += "{descr}\n\n".format(**method)
                if 'input' in method:
                    func.__doc__ += "Input: {input}\n\n".format(**method)
                if 'output' in method:
                    func.__doc__ += "Output: {output}\n\n".format(**method)
                if 'output2' in method:
                    func.__doc__ += "Output: {output2}\n\n".format(**method)
                func.__doc__ += '\n'
                return help(func)
        else:
            raise AttributeError("Method {method_name} not found".format(method_name=method_name))


class LBAPIMethod(object):
    __slots__ = ['_lb_session', '_method_name']

    def __init__(self, lb_session, method_name):
        self._lb_session = lb_session
        self._method_name = method_name

    def __call__(self, method_kwargs):
        return self._lb_session(self._method_name, method_kwargs)