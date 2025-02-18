**# Documentation : Utilisation de cURL pour interagir avec les API**

---

## 🌍 Introduction
cURL est un outil en ligne de commande permettant de transférer des données à l'aide de divers protocoles (**HTTP, HTTPS, FTP, etc.**). Il est couramment utilisé pour interagir avec des API **RESTful**.

---

## 📌 Installation

### 🐧 Sur Linux
```sh
sudo apt update && sudo apt install curl -y  # Debian/Ubuntu
sudo yum install curl -y  # CentOS/RHEL
```

### 🍏 Sur macOS
```sh
brew install curl
```

### 🖥️ Sur Windows
Téléchargez et installez cURL depuis : [🔗 Site officiel](https://curl.se/windows/)

---

## ⚡ Commandes de base

### 🔹 Effectuer une requête GET
```sh
curl https://api.example.com/resource
```

➡️ **Avec des en-têtes personnalisés**
```sh
curl -H "Authorization: Bearer TOKEN" -H "Accept: application/json" https://api.example.com/resource
```

### 🔹 Effectuer une requête POST
```sh
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/resource
```

### 🔹 Effectuer une requête PUT
```sh
curl -X PUT -H "Content-Type: application/json" -d '{"key":"new_value"}' https://api.example.com/resource/1
```

### 🔹 Effectuer une requête DELETE
```sh
curl -X DELETE https://api.example.com/resource/1
```

---

## 🛠️ Options utiles

### 💾 Sauvegarder une réponse dans un fichier
```sh
curl -o response.json https://api.example.com/resource
```

### 🔄 Suivre les redirections
```sh
curl -L https://api.example.com/resource
```

### 📑 Afficher les en-têtes de la réponse
```sh
curl -I https://api.example.com/resource
```

### 🔍 Augmenter la verbosité
```sh
curl -v https://api.example.com/resource
```

---

## 🔐 Authentification

### 🔑 Authentification par Basic Auth
```sh
curl -u username:password https://api.example.com/resource
```

### 🔑 Authentification par token
```sh
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/resource
```

---

## 🎯 Conclusion
cURL est un outil **puissant et flexible** pour interagir avec les API. Il permet d'**automatiser les requêtes HTTP** et de **manipuler les données efficacement**. Il est couramment utilisé pour **tester des endpoints** et **intégrer des services RESTful** dans des scripts.

🚀 **Explorez et automatisez vos appels API avec cURL !**

