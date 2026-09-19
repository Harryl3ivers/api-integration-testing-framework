import requests

class APIClient:
    def __init__(self,base_url):
        self.base_url = base_url

    def get_bookings(self):
        return requests.get(f"{self.base_url}/booking")
    
    def create_bookings(self,booking_data):
        return requests.post(f"{self.base_url}/booking",json=booking_data)
    
    def get_booking_id(self,booking_id):
        return requests.get(f"{self.base_url}/booking/{booking_id}")

    def login(self,username,password):
        return requests.post(f"{self.base_url}/auth",json={
            "username": username,
            "password":password
        })

    def update_booking(self,booking_id,booking_data,token):
        return requests.put(f"{self.base_url}/booking/{booking_id}",json=booking_data,headers={"Cookie": f"token={token}"})
    def delete_booking(self,booking_id,booking_data,token):
        return requests.delete(f"{self.base_url}/booking/{booking_id}",json=booking_data,headers={"Cookie":f"token={token}"})