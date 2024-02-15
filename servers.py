class Server:

    def __init__(self, password: str = None, max_players: int = 70, admin_password: str = "", server_map: str = ""):
        self.password = password
        self.max_players = max_players
        self.admin_password = admin_password
        self.map = server_map
