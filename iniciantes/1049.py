caracteristicas = str(input()).lower().strip()
caracteristicas_2 = str(input()).lower().strip()
caracteristicas_3 = str(input()).lower().strip()

entrada = (caracteristicas, caracteristicas_2, caracteristicas_3)

animal = {
    ("vertebrado", "ave", "carnivoro") : "aguia",
    ("vertebrado", "ave", "onivoro" ): "pomba",
    ("vertebrado", "mamifero", "onivoro"): "homem",
    ("vertebrado", "mamifero", "herbivoro"): "vaca",
    ("invertebrado", "inseto", "hematofago"): "pulga",
    ("invertebrado", "inseto", "herbivoro"): "lagarta",
    ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
    ("invertebrado", "anelideo", "onivoro"): "minhoca"
    }

print(animal[entrada])