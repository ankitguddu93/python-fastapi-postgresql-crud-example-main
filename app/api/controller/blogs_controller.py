from app.api.controller.base_controller import BaseController
from app.application.services.blogs_service import BlogService
from fastapi import APIRouter, Depends

class BlogController(BaseController):
    def __init__(self):
        super().__init__("/blogs", ["Blogs"], "blog", BlogService)
        self.router.add_api_route("/custom-endpoint", self.custom_endpoint, methods=["GET"])

    async def custom_endpoint(self):
        return {"message": "This is a custom blog endpoint"}
    
controller = BlogController()
router = controller.router