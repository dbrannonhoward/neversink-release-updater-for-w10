import importlib.util


class Trash:

    def load_runtime_module(self, module_name='neversink_spider_definition.py'):
        module_spec = importlib.util.find_spec(self.scraper_module)
        module_obj = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module_obj)
