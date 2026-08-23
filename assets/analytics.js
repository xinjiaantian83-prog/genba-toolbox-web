(() => {
  const STORAGE_KEY = "genba_toolbox_store_clicks";
  const FEATURE_STORAGE_KEY = "genba_toolbox_feature_request_events";

  function trackFeatureRequest(eventName, source) {
    const record = {
      event: eventName,
      source: source || "web",
      page_url: window.location.href,
      at: new Date().toISOString(),
    };
    try {
      const history = JSON.parse(localStorage.getItem(FEATURE_STORAGE_KEY) || "[]");
      history.push(record);
      localStorage.setItem(FEATURE_STORAGE_KEY, JSON.stringify(history.slice(-50)));
    } catch (_) {}
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(record);
  }

  window.genbaTrackFeatureRequest = trackFeatureRequest;
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

  const toggle = document.querySelector(".feature-request-toggle");
  const form = document.getElementById("feature-request-form");
  if (!toggle || !form) return;

  const status = form.querySelector(".feature-request-status");
  const submitButton = form.querySelector(".feature-request-submit");
  toggle.addEventListener("click", () => {
    const willOpen = form.hidden;
    form.hidden = !willOpen;
    toggle.setAttribute("aria-expanded", String(willOpen));
    toggle.textContent = willOpen ? "閉じる" : "欲しい機能を送る";
    if (willOpen) {
      trackFeatureRequest("feature_request_open", "web");
      form.querySelector("textarea[required]")?.focus();
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    status.className = "feature-request-status";
    if (!form.reportValidity()) {
      status.textContent = "必須項目を入力してください。";
      status.classList.add("is-error");
      return;
    }

    form.elements["送信日時"].value = new Date().toISOString();
    form.elements["現在ページURL"].value = window.location.href;
    status.textContent = "送信中です…";
    submitButton.disabled = true;

    try {
      const response = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok || result.success === false) throw new Error("request failed");
      trackFeatureRequest("feature_request_submit", "web");
      form.reset();
      status.textContent = "ありがとうございます。今後の開発候補として参考にさせていただきます。";
      status.classList.add("is-success");
    } catch (_) {
      status.textContent = navigator.onLine
        ? "送信に失敗しました。時間をおいて再度お試しください。"
        : "通信できません。接続を確認して再度お試しください。";
      status.classList.add("is-error");
    } finally {
      submitButton.disabled = false;
    }
  });
})();
