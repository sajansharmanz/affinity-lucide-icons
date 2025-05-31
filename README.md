# Affinity Lucide Icons

This repository contains a categorized **Assets file for Affinity Designer** featuring the full [Lucide Icons](https://lucide.dev/) set.

Icons are automatically sorted into subcategories based on the official Lucide metadata. Some icons appear in multiple categories to improve discoverability and UX when browsing the asset panel in Affinity Designer.

---

## 📦 What's Included

- `lucide-icons.afassets` — the ready-to-use Affinity Designer asset file
- `scripts/` — tools to regenerate and re-categorize icons yourself

---

## 📥 How to Import into Affinity Designer

1. Open **Affinity Designer**
2. Go to the **Assets Panel** (`View > Studio > Assets`)
3. Click the menu in the top-right corner of the panel
4. Choose **Import Assets**
5. Select the `lucide-icons.afassets` file
6. The icons will appear, organized by category

---

## 🔧 Regenerating the Asset File Yourself

If you'd like to generate a categorized icon set yourself:

### 1. Clone the [Lucide Icons repo](https://github.com/lucide-icons/lucide)

```bash
git clone https://github.com/lucide-icons/lucide
cd lucide
```

### 2. Add the Python Script

Place the provided `categorize_lucide_icons.py` script (found in the `scripts/` folder of this repo) into the root of the cloned Lucide repo.

### 3. Run the Script

```bash
python categorize_lucide_icons.py
```

This will generate a `categorized-icons/` folder, with each icon copied into folders that match its Lucide categories.
