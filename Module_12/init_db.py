import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(
            'mongodb+srv://Ivan_Grigorev:mongo_cloud_28.09_ig@cluster0.nzrg5.mongodb.net/'
            'myFirstDatabase?retryWrites=true&w=majority'
        )
db = client.module_12_hw
