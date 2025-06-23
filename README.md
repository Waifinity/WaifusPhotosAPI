
# 📸 Waifinity - Waifus Photos API

**API pública de imagens de waifus** do universo Waifinity, feita para ser leve, acessível e fácil de integrar em qualquer aplicação web, bot ou projeto de entretenimento.

---

## 🚀 Visão Geral

Esta API é baseada em um repositório GitHub com imagens organizadas por **categorias** e acompanhada por um arquivo `waifus.json` que mapeia todas as waifus disponíveis, incluindo sua **raridade** e rota completa.

Ela pode ser consumida por qualquer projeto, **sem necessidade de autenticação**, via [jsDelivr CDN](https://www.jsdelivr.com/).

---

## 🌐 Rotas base da API

### Imagens individuais:
```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/images/{categoria}/{imagem}.png
```

### JSON com mapeamento completo:
```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/waifus.json
```

---

## 📁 Estrutura de diretórios

As imagens estão dentro de `/images/` e organizadas por categoria:

```
/images
  ├── geral/
  ├── maid/
  ├── demon/
  ├── cyberpunk/
  └── gothic/
```

O arquivo `waifus.json` contém a estrutura assim:

```json
{
  "maid": [
    {
      "nome": "01.png",
      "url": "https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/images/maid/01.png",
      "raridade": "SR"
    }
  ]
}
```

---

## ✅ Como consumir a API com JavaScript

### 🔁 Puxar uma waifu aleatória de qualquer categoria com segurança:

```js
async function getWaifu(categoria = "maid") {
  const res = await fetch("https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/waifus.json");
  const data = await res.json();
  const lista = data[categoria];
  const index = Math.floor(Math.random() * lista.length);
  return lista[index]; // Objeto com nome, url e raridade
}
```

---

## 🎨 Visualizador com filtros

Você pode usar este painel para visualizar todas as waifus da API por **categoria e raridade**:

🔗 [Acesse o visualizador (versão HTML)]([https://seurepo.github.io/waifinity-viewer](https://waifinity.github.io/WaifusPhotosAPI/))

Ou use o código base pronto neste repositório para criar seu próprio painel.

---

## 📦 Recursos do JSON

O `waifus.json` é atualizado automaticamente por um script Python (`gerar_json.py`) que:
- Varre as pastas de imagens
- Atribui raridade aleatória (sem sobrescrever dados existentes)
- Garante compatibilidade total com o frontend

---

## ⚠️ Regras de Uso (LICENÇA)

- ✅ **Uso público e gratuito permitido**
- ❌ **Proibido uso comercial ou monetização direta**
- ❌ **Proibida revenda, reupload ou uso das imagens como conteúdo premium**
- ✅ Permitido em jogos, bots e projetos educacionais
- 📢 Atribuição opcional, mas bem-vinda: [@Waifinity](https://github.com/Waifinity)

---

## 📮 Sugestão de melhoria?

Contribuições são bem-vindas!  
Crie um fork, envie um pull request ou abra uma issue.

---

## ✨ Exemplo de rotas

Imagem individual:
```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/images/geral/01.png
```

JSON completo:
```
https://cdn.jsdelivr.net/gh/Waifinity/WaifusPhotosAPI/waifus.json
```

---

Feito com ❤️ pela equipe do projeto **Waifinity**.
