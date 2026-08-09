# Module Composition Chain Pattern
class ComposedModule:
    def __init__(self, modules: list):
        self.modules = modules
        
    def execute(self, loan_dict: dict) -> dict:
        result = loan_dict.copy()
        # Single loan flows through chain (Rule 5)
        for module in self.modules:
            result = module.process(result)
        return result
