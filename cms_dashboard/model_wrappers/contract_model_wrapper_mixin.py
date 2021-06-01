from django.apps import apps as django_apps
from .contract_model_wrapper import ContractModelWrapper


class ContractModelWrapperMixin:

    contract_model_wrapper_cls = ContractModelWrapper

    @property
    def contract_model_obj(self):
        contract_cls = django_apps.get_model('bhp_personnel.contract')
        contracts = contract_cls.objects.filter(
            identifier=self.identifier)
        if contracts:
            contract = contracts.order_by('created').last()
            return ContractModelWrapper(
               contract, next_url_name=self.next_url_name)
        else:
            return ContractModelWrapper(
                contract_cls(identifier=self.identifier),
                next_url_name=self.next_url_name)

