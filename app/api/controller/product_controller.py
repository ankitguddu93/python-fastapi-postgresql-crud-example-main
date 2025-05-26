from app.api.controller.base_controller import BaseController
from app.application.services.product_service import ProductService

class ProductController(BaseController):
    def __init__(self):
        super().__init__("/product", ["Product"], "product", ProductService)
         
controller = ProductController()
router = controller.router
 