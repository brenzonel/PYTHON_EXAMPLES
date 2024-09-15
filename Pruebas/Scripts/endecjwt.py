from jwcrypto.jwk import JWK
from jwt import JWT, jwk_from_dict

jwt = JWT() # Instancia de la clase JWK

def generate_key():
    jwk = JWK.generate(
        kty='RSA',
        size=2048,
        alg='RS256', # RS256, RS384, RS512, HS256, HS384, HS512
        use='sig',
        kid='1581' # Key ID
    )
    return jwk.export_private(as_dict=True), jwk.export_public(as_dict=True)
    # exporta ambas llaves privada y publica

def encode(data, key):
    #jwt = JWT() Ya se hizo la instancia arriba de la clase JWT
    jwk = jwk_from_dict(key)
    token = jwt.encode(data, jwk, alg="RS256", optional_headers={"typ": "JWT"})
    return token

def decode(token, key):
    #jwt = JWT() Ya se hizo la instancia arriba de la clase JWT
    jwk = jwk_from_dict(key)
    data = jwt.decode(token, jwk)
    return data

if __name__ == '__main__':
    data = {
        'sub': '1234567890',
        'name': 'Pruebas de cosas',
        'admin': True,
        'cosa': 'hola'
        #'exp': 1617225000 # Tiempo de expiracion
    }
    
    private_k, public_k = generate_key()
    """
    print("------------------------------------------------")
    print(private_k)
    print("------------------------------------------------")
    print(public_k)
    """
    token = encode(data, private_k)
    print(token)
    print("------------------------------------------------")
    payload = decode(token, public_k)
    print(payload)
    #print("------------------------------------------------")  
    #print(payload['sub'])  #obtener un valor en especifico
    print("------------------------------------------------")
    print(payload==data)