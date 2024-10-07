from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  # Время ожидания между запросами

    @task
    def index_page(self):
        self.client.get("https://kutuzov-art-hotel.ru/")  # Запрос главной страницы
        
    @task
    def rooms_page(self):
        self.client.get("https://kutuzov-art-hotel.ru/rooms-listing/")

    @task
    def attractions_page(self):
        self.client.get("https://kutuzov-art-hotel.ru/attractions/")

    @task
    def news_page(self):
        self.client.get(" https://kutuzov-art-hotel.ru/news/")

    @task
    def gallery_page(self):
        self.client.get(" https://kutuzov-art-hotel.ru/gallery")

    @task
    def contact_page(self):
        self.client.get(" https://kutuzov-art-hotel.ru/contact/")
