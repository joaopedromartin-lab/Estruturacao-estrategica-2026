# V4 Brand Book — Design System (referência verificada)

> Extraído de `BrandBook V4/index.html` (6761 linhas). Todos os valores abaixo foram lidos diretamente do arquivo, **não inferidos**. Use este documento como fonte da verdade para construir novos materiais alinhados ao brandbook.

---

## ⚠️ Importante: dois sistemas de cor coexistem

O arquivo mistura **dois conjuntos de tokens** que NÃO são intercambiáveis:

| Sistema | De onde vem | Quando usar |
|---|---|---|
| **Paleta oficial V4 (marca)** | Botões `data-copy` da seção `#color_palette` (linhas 4501–4730) | Sempre que for criar material novo da marca |
| **Tokens internos da página** | `--wp--preset--color--*` e `--ds-*` no `<style id="global-styles-inline-css">` | Para replicar visual exato do site brandbook |

A paleta oficial é o que define a marca. Os tokens internos são variações estilísticas usadas só na construção do site brandbook.

---

## 1. Paleta oficial V4 (marca)

### 1.1 Cor primária
| Token | HEX | RGB | CMYK |
|---|---|---|---|
| **Vermelho V4** | `#E50914` | `229, 9, 20` | `0, 99, 96, 0` |

### 1.2 Sistema (6 cores de suporte)
| Slot | HEX | Uso |
|---|---|---|
| Primário | `#E50914` | Identidade |
| Branco | `#FFFFFF` | Fundo / texto sobre escuro |
| Cinza claro | `#F2F2F2` | Fundos suaves, separadores |
| Cinza escuro | `#312D2D` | Texto secundário, fundos escuros |
| Marrom | `#280000` | Stop final em gradientes |
| Amarelo (CTA) | `#FFDD00` | CTA secundário, destaque |
| Preto | `#050505` | Texto principal sobre claro |

### 1.3 CTAs (verde + amarelo)
| Cor | HEX | Uso |
|---|---|---|
| **Verde CTA** | `#0E8420` | Botão primário (estado default) |
| **Amarelo CTA** | `#FFDD00` | CTA secundário, badges |

### 1.4 Gradientes digitais (paleta para web/screen)
Todos `linear-gradient(180deg, ...)`:

| Nome | Stops |
|---|---|
| **Peach Fade** | `#FFEBC8` 0% → `#FFB4A0` 50% → `#B4B4BE` 100% |
| **Red Dark** | `#FF481F` 0% → `#F0141E` 50% → `#280000` 100% |
| **Gray-to-Red** | `#E1DCDC` 0% → `#E88A70` ~33% → `#F0141E` ~66% → `#280000` 100% |
| **Red Bordô** | `#FF481F` 0% → `#650E0F` 100% |

### 1.5 Gradientes impressos (Pantone/CMYK)
| Nome | Stops |
|---|---|
| Print Red | `Pantone 3516 C` (CMYK 0 88 100 0) → `Pantone 3546 C` (CMYK 0 100 100 0) → `Pantone 2449 C` (CMYK 28 89 60 77) |
| Print Peach | `Pantone 664 C` (CMYK 6 8 0 0) → `Pantone 486 C` (CMYK 0 50 42 0) → `Pantone 3546 C` (CMYK 0 100 100 0) → `Pantone 2449 C` (CMYK 28 89 60 77) |
| Print Burgundy | `Pantone 3516 C` (CMYK 0 88 100 0) → `Pantone 1815 C` (CMYK 2 97 72 52) |

---

## 2. Tokens internos da página (WordPress preset stack)

Definidos em `<style id="global-styles-inline-css">` (linha 74). Servem para replicar o site do brandbook 1:1.

### 2.1 Custom properties — cores
```css
--wp--preset--color--black: #050505;
--wp--preset--color--cyan-bluish-gray: #abb8c3;
--wp--preset--color--white: #FFFFFF;
--wp--preset--color--yellow: #FDFF87;     /* ⚠️ NÃO é o amarelo da marca (#FFDD00). É um amarelo neon usado em arrows/links da página */
--wp--preset--color--light-gray: #F2F2F2;
--wp--preset--color--gray: #606060;
--wp--preset--color--dark-gray: #1E2124;  /* ⚠️ NÃO é o cinza escuro da marca (#312D2D) */
--wp--preset--color--black-70: #1c1c1cb3;
--wp--preset--color--white-70: #ffffffb3;
```

### 2.2 Custom properties — gradientes (`--ds-*` no `<style id="ds-showcase-styles">`)
```css
--ds-gradient-dark:    linear-gradient(135deg, #560303 0%, #7A0A02 40%, #FB2E0A 100%);
--ds-gradient-subtle:  linear-gradient(160deg, #560303 0%, #8B1205 50%, #C41E08 100%);
--ds-gradient-radial:  radial-gradient(ellipse at 20% 80%, #FB2E0A 0%, #7A0A02 40%, #560303 100%);
--ds-offwhite:         #FAF9F7;
```

Também definidos no preset WP:
```css
--wp--preset--gradient--black-radial-yellow: radial-gradient(circle at 100% 150%, rgba(253,255,135,1) 0%, rgba(5,5,5,1) 50%);
--wp--preset--gradient--brand-primary:       linear-gradient(135deg, #560303 0%, #7A0A02 40%, #FB2E0A 100%);
--wp--preset--gradient--brand-subtle:        linear-gradient(160deg, #560303 0%, #8B1205 50%, #C41E08 100%);
--wp--preset--gradient--brand-radial:        radial-gradient(ellipse at 20% 80%, #FB2E0A 0%, #7A0A02 40%, #560303 100%);
```

### 2.3 Hex literais recorrentes (não tokenizados, mas usados em hover/glow)
| Hex | Uso |
|---|---|
| `#FF6200` | Laranja de hover dos botões primários, glow |
| `#E55700` | Estado `:active` dos botões |
| `#FB2E0A` | Vermelho brilhante (arrow buttons, partículas, text-shadow) |
| `#560303` | Vermelho mais escuro do gradiente (também base do nav/header) |
| `#7A0A02` | Stop intermediário dos gradientes |
| `#8B1205`, `#C41E08` | Stops do gradient-subtle |
| `#DD0913` | Background do `.bb-manifesto` (variação do vermelho V4) |

---

## 3. Tipografia

### 3.1 Famílias carregadas

**IBM Plex Sans** (via Google Fonts, linha 116) — body, labels, interface
- Pesos: 300, 400, 500, 600, 700 + itálicos 400/500/600/700
- Alias no preset: `--wp--preset--font-family--pp-telegraf: 'IBM Plex Sans', sans-serif`
- ⚠️ O nome da variável é "pp-telegraf" (legado de um design anterior), mas a fonte real é **IBM Plex Sans**.

**Morganite** (self-hosted, linhas 120–141) — display / títulos de impacto
- Pesos: 500 (Medium), 600 (SemiBold), 700 (Bold)
- Arquivos: `assets/fonts/Morganite-Medium.ttf`, `Morganite-SemiBold.ttf`, `Morganite-Bold.ttf`
- Fallback em uso: `'Morganite', 'Anton', sans-serif`
- Aplicações: `.bb-manifesto__title`, `.bb-color__statement`, `.bb-type--red .bb-type__panel-title-main`, charset labels

**Monospace stack** (hints técnicos pequenos) — `ui-monospace, SFMono-Regular, Menlo, monospace`

### 3.2 Escala fluida (`--wp--preset--font-size--*`)
Todos usam `clamp(min, fluid, max)`:

| Token | Mínimo | Máximo | Fórmula completa |
|---|---|---|---|
| `--small` | 12px | 12px | `12px` (fixo) |
| `--medium` | 14px | 20px | `clamp(14px, 0.875rem + ((1vw - 5.8px) * 0.448), 20px)` |
| `--large` | 22px | 36px | `clamp(22.041px, 1.378rem + ((1vw - 5.8px) * 1.042), 36px)` |
| `--x-large` | 25px | 42px | `clamp(25.014px, 1.563rem + ((1vw - 5.8px) * 1.268), 42px)` |
| `--h-1` | 43.2px | 115px | `clamp(2.7rem, 2.7rem + ((1vw - 0.363rem) * 5.359), 115px)` |
| `--h-2` | 35px | 90px | `clamp(2.188rem, 2.188rem + ((1vw - 0.363rem) * 4.104), 90px)` |
| `--h-3` | 28px | 64px | `clamp(1.75rem, 1.75rem + ((1vw - 0.363rem) * 2.687), 64px)` |
| `--h-4` | 28px | 48px | `clamp(28px, 1.75rem + ((1vw - 5.8px) * 1.493), 48px)` |
| `--h-5` | 26px | 32px | `clamp(26px, 1.625rem + ((1vw - 5.8px) * 0.448), 32px)` |
| `--p-1` | 19.2px | 24px | `clamp(1.2rem, 1.2rem + ((1vw - 0.363rem) * 0.358), 24px)` |
| `--p-2` | 16px | 21px | `clamp(1rem, 1rem + ((1vw - 0.363rem) * 0.374), 21px)` |
| `--p-3` | 16px | 18px | `clamp(1rem, 1rem + ((1vw - 0.363rem) * 0.149), 18px)` |
| `--p-4` | 14px | 16px | `clamp(0.875rem, 0.875rem + ((1vw - 0.363rem) * 0.149), 16px)` |

### 3.3 Tamanhos display Morganite (em uso direto, fora dos tokens)
| Componente | Tamanho |
|---|---|
| `.bb-manifesto__title` | `clamp(72px, 12vw, 220px)`, `line-height: 0.9`, `letter-spacing: 0` |
| `.bb-type--red .bb-type__panel-title-main` | `clamp(44px, 4.2vw, 72px)` |
| Charset label | `clamp(15px, 1.2vw, 18px)` |

### 3.4 Defaults globais (body & headings)
```css
body {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: var(--wp--preset--font-size--p-1);
  font-weight: 400;
  line-height: 1.4;
  letter-spacing: -0.01em;
  color: var(--wp--preset--color--black-70);
  -webkit-font-smoothing: antialiased;
}
h1 { font-size: var(--h-1); line-height: 1;    letter-spacing: -0.03em; font-weight: 400; }
h2 { font-size: var(--h-2); line-height: 1.15; letter-spacing: -0.02em; margin-bottom: 0.5em; }
h3 { font-size: var(--h-3); line-height: 1.15; letter-spacing: -0.02em; }
h4 { font-size: var(--h-4); line-height: 1.15; letter-spacing: -0.02em; }
h5 { font-size: var(--h-5); line-height: 1.15; letter-spacing: -0.02em; }
h6 { font-size: var(--p-4); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }
```

---

## 4. Espaçamento

### 4.1 Tokens fluidos (`--wp--preset--spacing--*`)
| Token | Fórmula | Aproximado (mobile → desktop) |
|---|---|---|
| `--20` | `0.44rem` | ~7px (fixo) |
| `--30` | `24px` | 24px (fixo) |
| `--40` | `clamp(0.75rem, 0.1549rem + 1.6418vw, 2.125rem)` | 12px → 34px |
| `--50` | `clamp(1.625rem, 1.0299rem + 1.6418vw, 3rem)` | 26px → 48px |
| `--60` | `clamp(2rem, 1.2425rem + 2.0896vw, 3.75rem)` | 32px → 60px |
| `--70` | `clamp(3.125rem, 1.7724rem + 3.7313vw, 6.25rem)` | 50px → 100px |
| `--80` | `clamp(4.375rem, 2.2108rem + 5.9701vw, 9.375rem)` | 70px → 150px |
| `--90` | `clamp(5rem, 1.7537rem + 8.9552vw, 12.5rem)` | 80px → 200px |

### 4.2 Container & padding global
```css
--wp--style--global--content-size: 1720px;
--wp--style--global--wide-size:    1720px;
--wp--style--root--padding-right:  clamp(1.5rem, -0.556rem + 5.6716vw, 6.25rem);
--wp--style--root--padding-left:   clamp(1.5rem, -0.556rem + 5.6716vw, 6.25rem);
```
(≈24px no mobile, até 100px no desktop)

---

## 5. Border-radius

| Contexto | Valor | Onde |
|---|---|---|
| Buttons (pill) | `9999px` | `.wp-block-button__link`, `.bb-confidence`, toast |
| Images / featured | `25px` | `.wp-block-image img` global |
| Cards & panels | `15px`–`25px` | Posts, motion cards |
| Outline-large btn | `25px` | `::before` border |
| Color swatches | `4px` | `.bb-glass__panel` (sutileza) |
| Lucide grid items | `10px`–`14px` | Icons grid |
| Testimonial cards | `1.5625rem` (25px) | `.ds-testimonial__card` |

---

## 6. Sombras & glows

### 6.1 Box-shadows recorrentes
```css
/* Glow laranja (hover botão primário) */
box-shadow: 0 0 20px rgba(255, 98, 0, 0.4), 0 0 60px rgba(255, 98, 0, 0.15);
box-shadow: 0 0 24px rgba(255, 98, 0, 0.35), 0 0 60px rgba(255, 98, 0, 0.12);

/* :active mais comprimido */
box-shadow: 0 0 12px rgba(255, 98, 0, 0.5);

/* Card hover (vermelho) */
box-shadow: 0 12px 48px rgba(251, 46, 10, 0.25);
box-shadow: 0 12px 48px rgba(251, 46, 10, 0.3), 0 0 80px rgba(251, 46, 10, 0.1);

/* Outline-large hover */
box-shadow: 0 0 24px rgba(255, 98, 0, 0.3);

/* Card sutil */
box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
```

### 6.2 Text-shadows (glow em texto)
```css
text-shadow: 0 0 16px rgba(251, 46, 10, 0.5);   /* nav link hover */
text-shadow: 0 0 20px rgba(251, 46, 10, 0.4);   /* arrow button hover */
text-shadow: 0 0 14px rgba(253,255,135,0.85);   /* scramble lock flash (amarelo neon) */
```

### 6.3 Backdrop filter (glass)
```css
backdrop-filter: blur(20px) saturate(180%);   /* nav scrolled */
backdrop-filter: blur(8px);                    /* lightbox close */
backdrop-filter: blur(18px) saturate(180%);   /* componente glass exportável */
```

---

## 7. Animações

### 7.1 Todos os `@keyframes` definidos

```css
/* 1. Spin infinito — usado em ícones loading */
@keyframes ds-spin { to { transform: rotate(360deg); } }

/* 2. Pulse — ícones piscando */
@keyframes ds-pulse {
  0%, 100% { transform: scale(1);    opacity: 1; }
  50%      { transform: scale(1.18); opacity: 0.55; }
}

/* 3. Arrow slide — setas em CTAs */
@keyframes ds-arrow-slide {
  0%, 100% { transform: translateX(0); }
  50%      { transform: translateX(5px); }
}

/* 4. Stroke draw — desenho de ícones SVG */
@keyframes ds-draw {
  0%   { stroke-dashoffset: 32; opacity: 0.3; }
  55%  { stroke-dashoffset: 0;  opacity: 1; }
  100% { stroke-dashoffset: 0;  opacity: 1; }
}

/* 5. Marquee — scroll horizontal infinito de logos */
@keyframes marquee-scroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}

/* 6. Str bounce — seta de "scroll para baixo" no scroll text reveal */
@keyframes ds-str-bounce {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(10px); }
}

/* 7. Scramble lock flash — flash amarelo neon quando letra "trava" no scramble headline */
@keyframes bbScrambleLockFlash {
  0%   { text-shadow: 0 0 14px rgba(253,255,135,0.85); }
  60%  { text-shadow: 0 0 6px  rgba(253,255,135,0.35); }
  100% { text-shadow: 0 0 0    rgba(253,255,135,0); }
}
```

### 7.2 Durations padrão das animações
| Animação | Duração | Easing | Loop |
|---|---|---|---|
| `ds-spin` | `1s` | `linear` | ∞ |
| `ds-pulse` | `1.6s` | `ease-in-out` | ∞ |
| `ds-arrow-slide` | `1.2s` | `ease-in-out` | ∞ |
| `ds-draw` | `2.4s` | `cubic-bezier(.65,0,.35,1)` | ∞ |
| `marquee-scroll` | `30s` | `linear` | ∞ (pausa no hover) |
| `ds-str-bounce` | `2s` | `ease-in-out` | ∞ |
| `bbScrambleLockFlash` | `0.32s` | `ease-out` | uma vez por letra |

### 7.3 Curvas de easing (cubic-bezier) recorrentes
| Bezier | Onde |
|---|---|
| `cubic-bezier(0.23, 1, 0.32, 1)` | **PADRÃO** — cards, swatches, testimonials, transitions de overlay |
| `cubic-bezier(0.19, 1, 0.22, 1)` | Image zoom em hover (mais lenta, dramática) |
| `cubic-bezier(.455, .03, .515, .955)` | Outline-large button (elástico) |
| `cubic-bezier(.65, 0, .35, 1)` | Stroke draw (in-out forte) |

### 7.4 Durations padrão de transitions
| Velocidade | Duração | Quando |
|---|---|---|
| Rápida | `0.15s` – `0.25s` | Hover de copy-btn, feedback imediato |
| Média | `0.3s` – `0.4s` | Estado de botão, color transitions |
| Suave | `0.5s` | Background fades, card overlays |
| Dramática | `1s` | Image zoom on hover |

### 7.5 Marquee (mask gradient)
```css
.ds-marquee {
  -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 8%, #000 92%, transparent 100%);
          mask-image: linear-gradient(90deg, transparent 0%, #000 8%, #000 92%, transparent 100%);
}
.ds-marquee__track { animation: marquee-scroll 30s linear infinite; }
.ds-marquee:hover .ds-marquee__track { animation-play-state: paused; }
```

---

## 8. JavaScript — comportamentos e bibliotecas

### 8.1 Bibliotecas externas carregadas (linhas 5641–5649)
| Lib | CDN | Para que serve aqui |
|---|---|---|
| **GSAP 3.12.5** | `cdnjs gsap.min.js` | Scroll text reveal (char-by-char) |
| **ScrollTrigger** | `cdnjs ScrollTrigger.min.js` | Trigger das animações GSAP no scroll |
| **Splitting.js** | `unpkg splitting.min.js` | Quebra texto em `.char` para reveal |
| **AOS 2.3.1** | `unpkg aos.js` + `aos.css` | Fade-in genérico em scroll (`data-aos="fade-in"`) |
| **Lucide Icons** | `unpkg lucide.min.js` | Sistema de ícones (`[data-lucide]` → inline SVG) |

### 8.2 Comportamentos inline (script final, linhas 5653+)

| Função | Linha | O que faz |
|---|---|---|
| `AOS.init()` | 5657 | duration 1000ms, ease, once:false, offset 80 |
| `lucide.createIcons()` | 5661 | Substitui placeholders `[data-lucide]` por SVGs |
| `bbColorCopy()` | 5665 | Copy-to-clipboard global em qualquer `.bb-color-copy[data-copy]` + toast `#bb-color-toast` (1800ms) |
| `bbPromptCopy()` | 5705 | Copia prompt base de IA Liquid Glass (hardcoded multiline) |
| `bbPhotoPromptCopy()` | 5756 | Copia prompt base de fotografia (hardcoded multiline) |
| GSAP Scroll Reveal | 5803 | `.ds-reveal-text .char` → opacity 0.1 → 1, stagger 0.03s, scrub 1 |
| `.ds-copyable` swatches | 5827 | Copy + classe `.is-copied` por 1200ms |
| Glass HTML download | 5859 | Gera Blob de HTML standalone com componente glass e força download (`v4-glass-effect.html`) |
| Photo Tabs | 5952 | Tab system com escopo por seção, suporta data-direction prev/next |
| Constellation particles | 6450 | Canvas 2D injetado em `.ds-bg-gradient*`, 60 partículas, conexões a < 130px, interação com mouse (raio 180px), IntersectionObserver para pausar fora da viewport |
| `bbHeadlineScramble()` | 6598 | Para cada `.bb-headline-scramble` ou `.bb-scramble`: quebra em spans, anima cada char trocando por chars random até travar no final. Stagger 95ms ou `1100/letters` (long). Scramble dur 620ms por letra. IntersectionObserver threshold 0.25, dispara uma vez. Respeita `prefers-reduced-motion` |
| `bbMobileLightbox()` | 6697 | Tap em imagem (≤900px) abre overlay fullscreen |

### 8.3 Detalhes técnicos da Constellation
```js
const PARTICLE_COUNT  = 60;
const CONNECTION_DIST = 130;   // pixels
const MOUSE_RADIUS    = 180;   // pixels
// Cores das partículas (random distribuição):
// 35% → rgb(251,46,10)   brand orange-red
// 25% → rgb(255,80,40)   warm orange
// 20% → rgb(200,20,8)    deep red
// 20% → rgb(255,255,255) white accent
// Conexões: rgba(251,46,10, α) — α aumenta quando linha está perto do mouse
```

### 8.4 Detalhes técnicos do Scramble
```js
const pool = '!<>-_/\\[]{}=+*^?#$%ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
const startDelay   = 220;   // ms antes de começar
const scrambleDur  = 620;   // ms por letra
const tickInterval = 45;    // ms entre trocas de char aleatório
const stagger      = letters.length > 18 ? Math.max(30, 1100 / letters.length) : 95;
// Cada letra trava → ganha .bb-scramble-char--locked → dispara bbScrambleLockFlash (text-shadow amarelo)
```

---

## 9. Componentes catalogados

Mapeamento classe CSS → função. Use estas classes como ponto de partida ao construir telas novas.

### 9.1 Navegação
- **`.ds-nav`** — sticky top, gradiente vermelho, vira glass blur quando scrolled (`.is-scrolled`). Mobile: toggle `.ds-nav__toggle` + menu vertical em `.ds-nav__links`.

### 9.2 Botões
| Classe | Estilo |
|---|---|
| `.wp-block-button .wp-block-button__link` | Primário — verde `#0E8420`, hover laranja `#FF6200` com glow, circle-wipe `::after` |
| `.is-style-outline-large` | Outline com `::before` que encolhe pra 80% no hover + preenche laranja |
| `.is-style-arrow`, `.is-style-arrow-button` | Texto + seta SVG (`#FB2E0A`) que desliza no hover |
| `.bb-color-copy` / `.ds-copyable` | Qualquer elemento clicável para copiar `data-copy` |
| `.bb-glass__download-trigger` | Trigger pra baixar componente HTML standalone |

### 9.3 Cards
| Classe | Estilo |
|---|---|
| `.is-card-variation.has-link` | Card genérico — `::before` com gradient fades-in no hover, `translateY(-4px)` + glow vermelho |
| `.wp-block-post.case-study` | Imagem do post some no hover, fundo vira gradient vermelho |
| `.ds-testimonial__card` | Testimonial — `border-radius: 1.5625rem`, hover `translateY(-3px)` |
| `.bb-color__card`, `.bb-color__card--primary`, `--system`, `--cta`, `--digital`, `--print` | Cards da seção de cor (primário usa fundo `#E50914`) |
| `.bb-glass__panel`, `--image`, `--dark-image`, `--bordered`, `--image-card` | Painéis glass (componente reutilizável) |
| `.bb-confidence`, `--high` (#0E8420), `--medium` (#FF6200), `--low` (#C41E08), `--none` (gray) | Pills de "do & don't" |

### 9.4 Color swatches
| Classe | Função |
|---|---|
| `.ds-color-grid` / `.ds-color-swatch` | Grid 5 cols desktop / 3 mobile, hover scale 1.04, overlay com hex + copy btn |
| `.bb-color__system-cell` | Cell colorida na grid do sistema de 6 cores |
| `.bb-color__cta-block`, `--green` | Bloco CTA grande (verde ou amarelo) |
| `.bb-color__gradient-stop` (`--light`/`--dark`), `.bb-color__gradient-stop-btn` | Stops individuais dentro de gradientes mostráveis |
| `.bb-color__proportion-bar` | Barra de proporção visual de uso de cor |

### 9.5 Tipografia (showcase)
| Classe | Função |
|---|---|
| `.bb-type__panel` (`--red`) | Painel grande de showcase de fonte, gradient radial + linear |
| `.bb-type__charset-label` | Label "AaBb..." em Morganite uppercase |
| `.bb-type__download-btn` | Botão amarelo de download de font, hover vira vermelho |
| `.ds-type-row` / `.ds-type-name` / `.ds-type-preview` / `.ds-type-spec` | Tabela visual de tamanhos no DS showcase |

### 9.6 Animação de scroll
| Classe | Função |
|---|---|
| `.bb-headline-scramble`, `.bb-scramble` | Headline com efeito de scramble char-by-char (auto IntersectionObserver) |
| `.ds-reveal-text .char` | GSAP scroll-scrub reveal (opacity 0.1 → 1) |
| `data-aos="fade-in"` | AOS fade-in genérico |
| `.ds-anim--spin` / `--pulse` / `--slide` / `--draw` | Aplica keyframe nomeado em SVG ícones |

### 9.7 Outros
| Classe | Função |
|---|---|
| `.ds-marquee` / `.ds-marquee__track` / `.ds-marquee__logos` | Marquee infinito de logos |
| `.ds-constellation` | Wrapper canvas das partículas (auto-injetado) |
| `.bb-lightbox` (+ `.is-open`) | Lightbox mobile pra zoom de imagem |
| `.bb-color-toast` (id `bb-color-toast`) | Toast global "Copiado · #..." |
| `.ds-bg-gradient`, `.ds-bg-gradient-subtle`, `.ds-bg-gradient-radial`, `.ds-bg-offwhite` | Backgrounds de seção |
| `.ds-icon-foundation`, `.ds-lucide-grid`, `.ds-anim-icons` | 3 tipos de grid de ícones |

### 9.8 Componente Glass exportável (download)
O brandbook exporta um HTML standalone com o efeito glass via `.bb-glass__download-trigger`. Especificações Figma replicadas em CSS (linhas 5871–5930):

```
01 · Inner shadow — overlay, blur 150, FFFFFF 100%
02 · Inner shadow — overlay, blur 10,  FFFFFF 100%
03 · Inner shadow — overlay, blur 10,  FFFFFF 100%
04 · Inner shadow — overlay, blur 100, FFFFFF 100%
05 · Glass         — light -45° 80%, refraction 92, depth 23, dispersion 100, frost 5
06 · Drop shadow   — normal, X-5 Y5, blur 20, 000000 10%
```

CSS resultante:
```css
.v4-glass {
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(18px) saturate(180%);
  box-shadow:
    -5px 5px 20px rgba(0, 0, 0, 0.10),
    inset 0 0 150px rgba(255, 255, 255, 0.18),
    inset 0 0 100px rgba(255, 255, 255, 0.16),
    inset 0 0 10px  rgba(255, 255, 255, 0.45),
    inset 0 0 10px  rgba(255, 255, 255, 0.45);
}
.v4-glass::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.20) 0%, rgba(255,255,255,0.04) 45%, rgba(255,255,255,0.10) 100%);
  mix-blend-mode: overlay;
}
.v4-glass::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
```

---

## 10. Estrutura de seções do brandbook (âncoras)

Ordem do menu sticky:

| # | ID | Seção | Tipo visual |
|---|---|---|---|
| 1 | `#brand` | Brand (hero) | Full-bleed + scramble headline "Brand Book V4" |
| 2 | `#positioning` | Posicionamento | Full-bleed image + scramble |
| 3 | `#value_proposition` | Proposta de valor | Cards de pills (diagnostica, planeja, executa, gere em loop) |
| 4 | `#personality` | Personalidade | Sticky-stack 3 cards (direto e reto / sangue nos olhos / sempre à frente) |
| 5 | `#visual_identity` | Identidade visual | Full-bleed image hero |
| 6 | `#logo_applications` | Aplicações do logo | Composição de logos full-bleed |
| 7 | `#logo_main_version` | Logo principal | Glass panel + instruções + download |
| 8 | `#color_palette` | Cores | Cards: Primary, System, CTA, Digital gradients, Print gradients |
| 9 | `#color_palette_legacy` | (oculto) Showcase DS antigo | `display:none`, fica como backup |
| 10 | `#typography` | Tipografia | Painel red + samples |
| 11 | `#typography_morganite` | Morganite (display) | Showcase específico |
| 12 | `#photography` | Fotografia | Hero |
| 13 | `#photography_guidelines` | Diretrizes | Tabs + imagens |
| 14 | `#photography_official` | Fotos oficiais | Diretrizes específicas |
| 15 | `#photography_topics` | Luz / figurino / acting | Tab system |
| 16 | `#graphics` | Grafismos | Hero |
| 17 | `#graphics_glass` | Glass no Figma | Glass panel + tutorial |
| 18 | `#graphics_reverb` | Reverberação | Glass panel |
| 19 | `#graphics_perspective` | Perspectiva | Glass panel |
| 20 | `#graphics_ai` | Liquid Glass IA | Glass panel + prompt copy |
| 21 | `#iconography` | Ícones | Glass panel |
| 22 | `#iconography_system` | Sistema de ícones | Lucide grid |
| 23 | `#do_and_dont` | Do & Don't | Hero |
| 24 | `#logo_misuse` | Usos indevidos do logo | Confidence badges |
| 25 | `#contrast_guide` | Guia de contraste | Confidence badges |
| 26 | `#text_on_background` | Texto sobre fundo | Confidence badges |

---

## 11. Assets relevantes (`BrandBook V4/assets/`)

### Fontes (self-hosted)
- `assets/fonts/Morganite-Medium.ttf` (500)
- `assets/fonts/Morganite-SemiBold.ttf` (600)
- `assets/fonts/Morganite-Bold.ttf` (700)

### Logos
- `assets/v4-logo.svg`, `v4-logo-white.png`, `LogoV4Vermelha.svg`, `LogoV4Branca.svg`, `v4-logos.zip`

### CSS herdado (Spicerack WordPress theme)
- `style_b805307881ca.css` — block navigation
- `style-index_d2122a7a14b7.css` — block select content loop
- `style_92c8a3b039be.css` — block image
- `style_a405ed4bb8da.css` — block gallery
- `spicerack-wp-front-style_1190ae6c40d2.css` — front style geral

### Imagens-chave (para ideação)
- `Fueto.png`, `Foto Luegos.png` — hero images
- `LiquidglassIA.png`, `Modeloglass.png` — references glass effect
- `IconesFuetos.png`, `IconesSistema.png` — sistema de ícones
- `GrafismosImage.png`, `grafismolinhas.png`, `Reverbgradiente.png`, `PerspectiveGrafismofoto.png` — grafismos
- `Doedonts.png`, `Coressobrefundoerradas.png`, `Contrasteerrado.png`, `Repetição.png`, `Mocasozinha.png`, `Naologo.png` — do/don't
- Personas: `perso1.png`, `perso2.png`, `perso3.png`, `actingfoto.png`, `figurinofoto.png`, `luzfoto.png`

---

## 12. Receitas prontas (copy & paste)

### 12.1 Botão primário V4 (verde → hover laranja com glow)
```css
.btn-primary {
  background: #0E8420;
  color: #fff;
  border-radius: 9999px;
  padding: clamp(0.875rem, 0.5612rem + 0.8657vw, 1.7rem) clamp(1.625rem, 1.0299rem + 1.6418vw, 3rem);
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: var(--wp--preset--font-size--p-4, 14px);
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: background-color .5s cubic-bezier(0.23, 1, 0.32, 1),
              box-shadow      .5s cubic-bezier(0.23, 1, 0.32, 1);
}
.btn-primary:hover {
  background: #FF6200;
  box-shadow: 0 0 24px rgba(255, 98, 0, 0.35), 0 0 60px rgba(255, 98, 0, 0.12);
}
.btn-primary:active { background: #E55700; }
```

### 12.2 Seção com gradient hero V4
```css
.hero-v4 {
  background: linear-gradient(135deg, #560303 0%, #7A0A02 40%, #FB2E0A 100%);
  color: #fff;
  padding: var(--wp--preset--spacing--90, 80px) clamp(1.5rem, -0.556rem + 5.6716vw, 6.25rem);
  position: relative;
  overflow: hidden;
}
.hero-v4 h1 {
  font-family: 'Morganite', 'Anton', sans-serif;
  font-size: clamp(72px, 12vw, 220px);
  font-weight: 700;
  line-height: 0.9;
  letter-spacing: 0;
  text-transform: uppercase;
  color: #fff;
}
```

### 12.3 Card hover com gradient overlay
```css
.card-v4 {
  position: relative;
  overflow: hidden;
  border-radius: 25px;
  background: #fff;
  padding: var(--wp--preset--spacing--60, 32px);
  transition: transform .4s cubic-bezier(0.23, 1, 0.32, 1),
              box-shadow .5s cubic-bezier(0.23, 1, 0.32, 1);
}
.card-v4::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(135deg, #560303 0%, #7A0A02 40%, #FB2E0A 100%);
  opacity: 0;
  transition: opacity .5s cubic-bezier(0.23, 1, 0.32, 1);
  z-index: 0;
}
.card-v4 > * { position: relative; z-index: 1; }
.card-v4:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 48px rgba(251, 46, 10, 0.3), 0 0 80px rgba(251, 46, 10, 0.1);
  color: #fff;
}
.card-v4:hover::before { opacity: 1; }
```

### 12.4 Marquee de logos infinito
```html
<div class="marquee">
  <div class="marquee__track">
    <div class="marquee__logos"><!-- repete logos --></div>
    <div class="marquee__logos"><!-- duplicado pra loop seamless --></div>
  </div>
</div>
<style>
.marquee {
  overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 8%, #000 92%, transparent 100%);
          mask-image: linear-gradient(90deg, transparent 0%, #000 8%, #000 92%, transparent 100%);
}
.marquee__track { display: flex; width: max-content; animation: marquee-scroll 30s linear infinite; }
.marquee:hover .marquee__track { animation-play-state: paused; }
.marquee__logos { display: flex; gap: clamp(3rem, 5vw, 6rem); padding-right: clamp(3rem, 5vw, 6rem); }
@keyframes marquee-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
</style>
```

---

## 13. Checklist rápido pra novos materiais V4

Antes de publicar qualquer coisa nova alinhada ao brandbook, valide:

- [ ] Cor principal vermelho **`#E50914`** (não `#FB2E0A`, que é apenas accent)
- [ ] CTA primário usa **verde `#0E8420`** com hover **laranja `#FF6200`** + glow
- [ ] Tipografia: **IBM Plex Sans** body / **Morganite** display
- [ ] Headlines display em uppercase, letter-spacing `0`, line-height `0.9`
- [ ] Espaçamento usa tokens fluidos (`clamp`), não pixels fixos
- [ ] Container max-width `1720px`, padding horizontal `clamp(1.5rem, ..., 6.25rem)`
- [ ] Gradients usam stops oficiais (135deg dark / 160deg subtle / radial 20% 80%)
- [ ] Border-radius: pill `9999px` em buttons, `25px` em imagens/cards
- [ ] Hover de elementos clicáveis usa easing `cubic-bezier(0.23, 1, 0.32, 1)`
- [ ] Headlines de hero podem usar scramble (classe `.bb-headline-scramble` ou `.bb-scramble`)
- [ ] Seções gradient consideram partículas constellation pra dar vida
