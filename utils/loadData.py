RESOURCES = [
    "PRODUCTS",
    "ORDER",
    "PAYMENT",
    "USER"
]

ROLES = {
    "ADMIN": [
        {
            "RESOURCE" : "PRODUCTS",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        },{
            "RESOURCE" : "ORDER",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        },{
            "RESOURCE" : "PAYMENT",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        },{
            "RESOURCE" : "USER",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        },
    ],
    "CATALOGUE_MANAGER" : [
        {
            "RESOURCE" : "PRODUCTS",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        }
    ],
    "ORDER_MANAGER": [
        {
            "RESOURCE" : "ORDER",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        }
    ],
    "ORDER_USER": [
        {
            "RESOURCE" : "ORDER",
            "ACCESS" : ["READ",]
        }
    ],
    "PAYMENT_USER": [
        {
            "RESOURCE" : "PAYMENT",
            "ACCESS" : ["READ",]
        }
    ],
    "PAYMENT_MANAGER": [
        {
            "RESOURCE" : "PAYMENT",
            "ACCESS" : ["READ", "WRITE", "DELETE"]
        }
    ],
    "ANALYTICS_MANAGER": [
        {
            "RESOURCE" : "PRODUCTS",
            "ACCESS" : ["READ",]
        },{
            "RESOURCE" : "ORDER",
            "ACCESS" : ["READ",]
        },{
            "RESOURCE" : "PAYMENT",
            "ACCESS" : ["READ",]
        },
    ]
}

USERS = {
    "admin":[ "ADMIN"]
}