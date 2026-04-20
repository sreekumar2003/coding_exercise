/* Modern PPT Generator – front-end logic */

// ── Tab switching ─────────────────────────────────────────────────────────────
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => {
      t.classList.remove('active');
      t.setAttribute('aria-selected', 'false');
    });
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    tab.setAttribute('aria-selected', 'true');
    const target = document.getElementById('tab-' + tab.dataset.tab);
    if (target) target.classList.add('active');
  });
});

// ── Theme pills ───────────────────────────────────────────────────────────────
document.querySelectorAll('.pill').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
  });
});

// ── File input / drag-and-drop ────────────────────────────────────────────────
const dropZone   = document.getElementById('dropZone');
const fileInput  = document.getElementById('fileInput');
const fileNameEl = document.getElementById('fileName');
const browseBtn  = document.getElementById('browseBtn');

browseBtn.addEventListener('click', () => fileInput.click());
dropZone.addEventListener('click', e => { if (e.target !== browseBtn) fileInput.click(); });

fileInput.addEventListener('change', () => {
  if (fileInput.files[0]) showFileName(fileInput.files[0].name);
});

dropZone.addEventListener('dragover', e => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', e => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file) {
    const dt = new DataTransfer();
    dt.items.add(file);
    fileInput.files = dt.files;
    showFileName(file.name);
  }
});

function showFileName(name) {
  fileNameEl.textContent = '📄 ' + name;
}

// ── Helpers ───────────────────────────────────────────────────────────────────
const errorBanner  = document.getElementById('errorBanner');

function showError(msg) {
  errorBanner.textContent = '⚠ ' + msg;
  errorBanner.hidden = false;
}
function clearError() {
  errorBanner.hidden = true;
  errorBanner.textContent = '';
}

function buildFormData() {
  const fd = new FormData(document.getElementById('mainForm'));
  // If in text tab, clear file; if in upload tab, clear text
  const activeTab = document.querySelector('.tab.active').dataset.tab;
  if (activeTab === 'text') {
    fd.delete('file');
  } else {
    fd.delete('plain_text');
  }
  return fd;
}

// ── Preview ───────────────────────────────────────────────────────────────────
const previewBtn     = document.getElementById('previewBtn');
const previewSection = document.getElementById('previewSection');
const slideGrid      = document.getElementById('slideGrid');
const slideCount     = document.getElementById('slideCount');

previewBtn.addEventListener('click', async () => {
  clearError();
  previewBtn.disabled = true;
  previewBtn.innerHTML = '<span class="spinner"></span> Loading…';

  try {
    const res = await fetch('/preview', { method: 'POST', body: buildFormData() });
    const data = await res.json();

    if (!res.ok) { showError(data.error || 'Preview failed.'); return; }

    renderPreview(data.slides, data.theme);
    previewSection.hidden = false;
    previewSection.scrollIntoView({ behavior: 'smooth' });
  } catch (err) {
    showError('Network error: ' + err.message);
  } finally {
    previewBtn.disabled = false;
    previewBtn.innerHTML = '👁 Preview Slides';
  }
});

function renderPreview(slides, theme) {
  slideGrid.innerHTML = '';
  slideCount.textContent = `(${slides.length} slides · ${theme} theme)`;

  slides.forEach((slide, i) => {
    const card = document.createElement('div');
    card.className = `slide-card layout-${slide.layout}`;

    const badgeMap = {
      title:   'badge-title',
      section: 'badge-section',
      bullets: 'badge-bullets',
      content: 'badge-content',
    };

    const bullets = (slide.bullets || []).slice(0, 4)
      .map(b => `<li>${escHtml(b)}</li>`).join('');
    const moreBullets = slide.bullets && slide.bullets.length > 4
      ? `<li style="opacity:.5">+ ${slide.bullets.length - 4} more…</li>` : '';

    card.innerHTML = `
      <div class="slide-num">Slide ${i + 1}</div>
      <span class="badge ${badgeMap[slide.layout] || 'badge-content'}">${slide.layout}</span>
      <div class="slide-title">${escHtml(slide.title)}</div>
      ${bullets || moreBullets ? `<ul class="slide-bullets">${bullets}${moreBullets}</ul>` : ''}
    `;
    slideGrid.appendChild(card);
  });
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Generate & download ───────────────────────────────────────────────────────
const mainForm    = document.getElementById('mainForm');
const generateBtn = document.getElementById('generateBtn');

mainForm.addEventListener('submit', async e => {
  e.preventDefault();
  clearError();
  generateBtn.disabled = true;
  generateBtn.innerHTML = '<span class="spinner"></span> Generating…';

  try {
    const res = await fetch('/generate', { method: 'POST', body: buildFormData() });

    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      showError(data.error || `Server error ${res.status}`);
      return;
    }

    // Trigger download
    const blob = await res.blob();
    const disposition = res.headers.get('Content-Disposition') || '';
    const nameMatch = disposition.match(/filename\*?=(?:UTF-8'')?["']?([^"';\n]+)/i);
    const fileName = nameMatch ? decodeURIComponent(nameMatch[1]) : 'presentation_modern.pptx';

    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = fileName;
    document.body.appendChild(a); a.click();
    a.remove(); URL.revokeObjectURL(url);

  } catch (err) {
    showError('Network error: ' + err.message);
  } finally {
    generateBtn.disabled = false;
    generateBtn.innerHTML = '✨ Generate &amp; Download';
  }
});
