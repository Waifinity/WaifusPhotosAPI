
# 📸 Waifinity - Waifus Photos API

**API pública de imagens de waifus** do universo Waifinity, feita para ser leve, acessível e fácil de integrar em qualquer aplicação web, bot ou projeto de entretenimento.

---

## 🚀 Visão Geral

Esta é uma API baseada em repositório GitHub + CDN da [jsDelivr](https://www.jsdelivr.com/), com imagens organizadas por categorias.  
Ela serve **imagens diretamente** por URL, sem necessidade de autenticação ou backend.

---

## 🌐 Rota base da API

A rota base para as imagens é:

```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/
```

---

## 📁 Estrutura de diretórios

As imagens estão organizadas por **categorias**.  
Exemplo de categorias atuais:

```
/geral
/demon
/maid
/gothic
/cyberpunk
```

Cada categoria contém imagens em formato `.png` numeradas:

```
/geral/01.png
/geral/02.png
/maid/01.png
```

---

## ✅ Exemplo de uso direto

Você pode usar qualquer imagem diretamente com HTML:

```html
<img src="https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/geral/01.png" alt="Waifu" />
```

---

## 🧠 Como fazer requisições com JavaScript

### 🔁 Puxando uma imagem aleatória de uma categoria:

```js
const totalImagens = 10; // número de imagens disponíveis na categoria
const randomId = Math.floor(Math.random() * totalImagens) + 1;
const categoria = "geral";
const imageUrl = `https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/${categoria}/${String(randomId).padStart(2, '0')}.png`;

document.getElementById("waifu").src = imageUrl;
```

### HTML correspondente:
```html
<img id="waifu" alt="Sua waifu aleatória aparecerá aqui" />
```

---

## 📦 Requisições dinâmicas (opcional)

Caso queira criar uma **API personalizada em JSON**, você pode criar um arquivo `waifus.json` contendo:

```json
{
  "waifus": [
    {
      "nome": "Yumi",
      "categoria": "maid",
      "image": "https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/maid/01.png",
      "raridade": "SR"
    }
  ]
}
```

Isso facilita filtros por raridade ou nome.

---

## ⚠️ Regras de Uso (LICENÇA)

- ✅ **Uso público e gratuito permitido**
- ❌ **Proibido uso comercial ou monetização direta**
- ❌ **Proibida revenda, reupload ou uso das imagens como conteúdo premium**
- ✅ Pode ser usada em projetos educacionais, jogos pessoais e bots
- 📢 Atribuição opcional, mas bem-vinda: [@Waifinity](https://github.com/Waifinity)

---

## 📮 Sugestão de melhoria?

Contribuições são bem-vindas!  
Crie um fork, envie um pull request ou abra uma issue.

---

## ✨ Exemplo de rota funcional

```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/geral/01.png
```

---

Feito com ❤️ pela equipe do projeto **Waifinity**.
