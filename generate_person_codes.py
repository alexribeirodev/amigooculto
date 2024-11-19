import pandas as pd
import os
import uuid
from crypto_utils import encrypt_text


def generate_person_codes():
    names = os.getenv("NAMES", "Alex,Nayara,Divina,Reyner,Lorena,Lucineia,Antônio")
    names = names.split(",")

    df = pd.DataFrame({"name": names})
    df = df.sample(frac=1).reset_index(drop=True)

    for i, row in df.iterrows():
        if i == 0:
            df.loc[i, "to"] = encrypt_text(df.loc[len(df) - 1, "name"])
        else:
            df.loc[i, "to"] = encrypt_text(df.loc[i - 1, "name"])
        # Generate UUID for unique code
        df.loc[i, "unique_code"] = str(uuid.uuid4())
    print(df)

    df.to_csv("names.csv", index=False)
