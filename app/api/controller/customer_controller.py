from app.api.controller.base_controller import BaseController
from app.application.services.customer_service import CustomerService

class CustomerController(BaseController):
    def __init__(self):
        super().__init__("/customer", ["Customer"], "customer", CustomerService)
         
controller = CustomerController()
router = controller.router
 