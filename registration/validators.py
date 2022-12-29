
import sys
sys.path.append("..")

from .models import Register
from .forms import RegisterForm

from datetime import date

class Validator:
    def __init__(self, model: object, *args, **kwargs) -> None:
        self.model = model
        self.args = args
        self.kwargs = kwargs
        self.data = {}


    def is_valid(self) -> bool:
        label = []
        for key, value in self.model.info(self).items():
            for inner_key, inner_value in value[1].items():
                if isinstance(inner_value, bool):
                    if self.__getattribute__(inner_key)(value=self.args[0][key], limit=inner_value, key=key) is inner_value:
                        label.append(True)
                    else:
                        self.data.update({
                            'request.POST': self.args
                        })
                        return False
                else:
                    if self.__getattribute__(inner_key)(value=self.args[0][key], limit=inner_value, key=key):
                        label.append(True)
                    else:
                        self.data.update({
                            'request.POST': self.args
                        })
                        return False
                
        if self.args[0]['password'] == self.args[0]['confirm_password']:
            label.append(True)
        else:
            return False

        if sum(label) == len(label):
            return True
        else:
            return False


    def with_error(self):
        return self.data


    def is_alpha(self, value, limit, key, *args, **kwargs) -> bool:
        not_allowed_symbols = [
            '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
            '_', '-', '+', '=', '\\' ,'/', '|', '?', '<', '>', '.', ',',
            '{', '[', ']', '}', "'", '"', ';', ':'
        ]
        if limit:
            label = False
            for item in value:
                try:
                    int(item)
                    return False
                except Exception:
                    if item not in not_allowed_symbols:
                        label = True
                    else:
                        return False
            return label
        else:
            label = False
            for item in value:
                try:
                    int(item)
                    label = False
                except Exception:
                    return True
            return label


    def is_numeric(self, value, limit, key, *args, **kwargs) -> bool:
        for item in value:
            label = False
            try:
                int(item)
                label = True
            except Exception:
                return False
            return label


    def unique(self, value, limit, key, *args, **kwargs) -> bool:
        try:
            Register.objects.get(email=value)
            return False
        except Exception:
            return True


    def max_length(self, value, limit, key, *args, **kwargs) -> bool:
        return True if len(value) <= limit else False


    def null(self, value, limit, key, *args, **kwargs):
        if limit:
            if len(value) == 0:
                self.args[0][key] = None
                return True
            return True
        else:
            if len(value) == 0:
                return False
            else:
                return True


    def choices(self, value, limit, key, *args, **kwargs):
        choice_menu = [item[0] for item in limit]
        return True if value.lower() in choice_menu else False


    def alpha_numeric(self, value, limit, key, *args, **kwargs):
        if limit:
            label = []
            for item in value:
                try:
                    int(item)
                    label.append('int')
                except Exception:
                    label.append('str')
            if 'int' in label:
                if 'str' in label:
                    return True
            else:
                return False


    def min_year(self, value, limit, key, *args, **kwargs):
        today = date.today().year
        year = int(value.split('-')[0])
        return True if today - int(limit) >= year else False


    def max_year(self, value, limit, key, *args, **kwargs):
        today = date.today().year
        year = int(value.split('-')[0])
        return True if today - int(limit) <= year else False


    def is_empty(self, value, limit, key,  *args, **kwargs) -> bool:
        if not limit:
            for value in self.args[0].values(): 
                return True if len(value) == 0 else False
        else:
            return True


    def save(self, request):
        form = RegisterForm(request)
        if form.is_valid():
            form.save()
            return True
        else:
            return False


    def is_true(self):
        try:
            user = Register.objects.get(email=self.args[0]['email'])
            if user.email == self.args[0]['email'] and user.password == self.args[0]['password']:
                return True
            else:
                return False
        except Exception:
            return False


    def __str__(self):
        return self.args[0]['first_name'] + ' ' + self.args[0]['last_name']