**🔗 Différences entre HTTP et HTTPS**

| **Protocole** | **HTTP** | **HTTPS** |
|--------------|---------|----------|
| **Sécurité** | Non chiffré, vulnérable aux attaques | Chiffré via SSL/TLS, sécurisé |
| **URL** | Commence par `http://` | Commence par `https://` |
| **Usage** | Sites non sensibles | Transactions, authentifications |

---

**📊 Structure d'une requête et d'une réponse HTTP**

**1️⃣ Requête HTTP (Exemple GET)**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**2️⃣ Réponse HTTP (Exemple 200 OK)**
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>
<head><title>Exemple</title></head>
<body><h1>Bonjour, monde!</h1></body>
</html>
```

---

**🌐 Liste des méthodes HTTP et leurs usages**

| **Méthode** | **Description** | **Cas d'utilisation** |
|------------|----------------|-------------------|
| **GET** | Récupère des données | Charger une page web, obtenir des données d'une API |
| **POST** | Envoie des données | Soumission d'un formulaire, création de ressources |
| **PUT** | Met à jour une ressource | Modification d'un profil utilisateur |
| **DELETE** | Supprime une ressource | Suppression d'un compte |
| **PATCH** | Modifie partiellement une ressource | Mise à jour d'un champ particulier |
| **HEAD** | Récupère uniquement les en-têtes | Tester la validité d'une URL |

---

**🔢 Codes de statut HTTP courants**

| **Code** | **Description** | **Scénario** |
|--------|--------------|-----------|
| **200** | OK | Requête réussie |
| **301** | Moved Permanently | Redirection permanente d'une URL |
| **400** | Bad Request | Requête mal formée |
| **401** | Unauthorized | Accès refusé sans authentification |
| **403** | Forbidden | Accès interdit même avec authentification |
| **404** | Not Found | Page ou ressource introuvable |
| **500** | Internal Server Error | Erreur interne du serveur |
| **503** | Service Unavailable | Serveur temporairement indisponible |

Ce document offre un résumé clair et visuel des principales différences entre HTTP et HTTPS, ainsi qu'une explication des requêtes/réponses HTTP, des méthodes courantes et des codes de statut utilisés dans les communications web. 📈

