import os

class ConfigManager:
    def getDefaultOrg(self):
        return os.getenv('USER', 'DefaultOrg')

    def getDefaultYear(self):
        from datetime import datetime
        return datetime.now().year