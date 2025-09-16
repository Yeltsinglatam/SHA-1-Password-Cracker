from hashlib import sha1

def crack_sha1_hash(target_hash, use_salts=False):
    target_hash = (target_hash or "").lower()

    try:
        # Cargar contraseñas una sola vez
        with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
            passwords = [line.strip() for line in f if line.strip()]

        if use_salts:
            # Cargar sales una sola vez
            with open("known-salts.txt", "r", encoding="utf-8") as f:
                salts = [line.strip() for line in f if line.strip()]

            # Probar salt+password y password+salt
            for pwd in passwords:
                for s in salts:
                    if sha1((s + pwd).encode("utf-8")).hexdigest() == target_hash:
                        return pwd
                    if sha1((pwd + s).encode("utf-8")).hexdigest() == target_hash:
                        return pwd
        else:
            # Probar sin sal
            for pwd in passwords:
                if sha1(pwd.encode("utf-8")).hexdigest() == target_hash:
                    return pwd

        return "PASSWORD NOT IN DATABASE"

    except FileNotFoundError:
        # No imprimir ni lanzar: FCC espera este string
        return "PASSWORD NOT IN DATABASE"
