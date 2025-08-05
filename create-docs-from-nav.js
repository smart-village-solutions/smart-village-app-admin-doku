const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const mkdocsPath = path.join(__dirname, "mkdocs.yml");
const docsDir = path.join(__dirname, "docs");

function ensureDir(filePath) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function processNav(nav, parent = "") {
  for (const item of nav) {
    if (typeof item === "string") continue;
    for (const [title, value] of Object.entries(item)) {
      if (typeof value === "string") {
        const filePath = path.join(docsDir, value);
        ensureDir(filePath);
        if (!fs.existsSync(filePath)) {
          fs.writeFileSync(filePath, `# ${title}\n`);
          console.log("✓ Datei erstellt:", value);
        } else {
          console.log("• Datei bereits vorhanden:", value);
        }
      } else if (Array.isArray(value)) {
        processNav(value, path.join(parent, title));
      }
    }
  }
}

function main() {
  if (!fs.existsSync(mkdocsPath)) {
    console.error("mkdocs.yml nicht gefunden!");
    return;
  }

  const ymlContent = fs.readFileSync(mkdocsPath, "utf8");
  const config = yaml.load(ymlContent);

  if (!config.nav) {
    console.error("Keine 'nav'-Sektion in mkdocs.yml gefunden!");
    return;
  }

  processNav(config.nav);
  console.log("✅ Verarbeitung abgeschlossen.");
}

main();
