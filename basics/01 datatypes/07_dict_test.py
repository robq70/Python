config = {
    "website": "example.com",
    "dbType": "mysql",
    "dbUser": "admin",
    "dbPassword": "1234",
}

print(len(config))
print(config["dbType"])

for key, value in config.items():
    print(key + " " + value)
