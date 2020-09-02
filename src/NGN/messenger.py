from . import FacebookMessenger, DevMessenger


FACEBOOK_CHECK_TOKEN = 'VERIFY_TOKEN'
FACEBOOK_AUTH_TOKEN = (
        'EAAKnsCzlM7wBAM0waYVmDwMFMg1s6GMDoDCXSV1ZADQ9xxhzonZAKhHmJ8TZBhN58IKd'
        '9cUlAprdc1lBPFhXmRQTmBv8aNZAq6ko2wVTwF0xxOKDkwrD2iRKeQEVzjCk2J6eNAfCz'
        'kD2uQ4rGv96QwZC24p8sZC2GrS4uv25WNgQZDZD')
# messenger = FacebookMessenger(FACEBOOK_AUTH_TOKEN)
messenger = DevMessenger()
