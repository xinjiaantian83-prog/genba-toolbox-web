(() => {
  const STORAGE_KEY = "genba_toolbox_store_clicks";
  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[data-store]");
    if (!link) return;
    const record = {
      store: link.dataset.store,
      page: link.dataset.page || document.body.dataset.page || "unknown",
      referrer: document.referrer || "direct",
      at: new Date().toISOString(),
    };
    try {
      const history = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      history.push(record);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(history.slice(-50)));
    } catch (_) {}
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: "store_click", ...record });
  });
})();
