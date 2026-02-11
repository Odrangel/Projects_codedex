def google_serch(query):
    """" Simula una busqueda en google"""
    if not query:
        raise ValueError("la consulta no puede estar vacia")
    results = {
            "python":["python.org", "tutorial python", "aprende python"],
            "java":["java.com", "tutorial java", "aprende java"],
            "c++":["c++.com", "tutorial c++", "aprende c++"]
        }
    return results.get(query.lower(),[])

print(google_serch("c++"))