/* Nieuwe wireframes Productontwikkeling & Inkoop (71 schermen) binnen de werkplek.
   De schermen staan in wireframes.html; hier worden ze als route #wf.<SCHERM> getoond
   onder Productontwikkeling & Inkoop in de zijbalk. */
const WF_MODULE_START = {
  DA: "DA01", PK: "PK01", RP: "RP01", RD: "RD01", PL: "PL01", CA: "CA01",
  LV: "LV01", AB: "AB01", ON: "ON01", CT: "CT01", AU: "AU01",
}
function wfNavRoute(id) {
  const screen = String(id || "DA01")
  if (screen === "flows" || screen === "index") return "wf." + screen
  return "wf." + (WF_MODULE_START[screen.slice(0, 2).toUpperCase()] || "DA01")
}
function wfTitle(id) {
  const link = document.querySelector(`#nav a[href="#${wfNavRoute(id)}"]`)
  return link ? link.textContent.trim() : "Wireframes"
}
PAGES.wf = (id) => {
  const screen = /^([A-Z]{2}\d{2}|flows|index)$/.test(id || "") ? id : "DA01"
  return `<h1 class="sr-only">Wireframe ${esc(screen)}</h1><div class="wf-frame-wrap"><iframe id="wf-frame" class="wf-frame" title="Wireframe ${esc(screen)} · Productontwikkeling & Inkoop" src="wireframes.html?embed=1#/${encodeURIComponent(screen)}"></iframe></div>`
}
// Het ingebedde scherm meldt route, hoogte en meldingen aan de werkplek.
window.addEventListener("message", (ev) => {
  const frame = document.getElementById("wf-frame")
  if (!frame || ev.source !== frame.contentWindow || !ev.data || typeof ev.data !== "object") return
  const { wfRoute, wfHeight, wfToast, wfTop } = ev.data
  if (wfHeight) frame.style.height = Math.max(600, Math.ceil(wfHeight)) + "px"
  if (wfToast) toast(String(wfToast))
  if (wfTop) window.scrollTo({ top: 0, behavior: "auto" })
  if (wfRoute && parseHash().p === "wf" && parseHash().id !== wfRoute) {
    history.replaceState(null, "", "#wf." + wfRoute)
    const target = wfNavRoute(wfRoute)
    document.querySelectorAll("#nav a").forEach((a) => {
      if (a.getAttribute("href") === "#" + target) a.setAttribute("aria-current", "page")
      else if (a.getAttribute("href")?.startsWith("#wf.")) a.removeAttribute("aria-current")
    })
    wfCrumb(wfRoute)
    lastRoute = "wf." + wfRoute + "."
  }
})
function wfCrumb(id) {
  const crumb = document.querySelector("#view .crumb")
  if (!crumb) return
  const route = wfNavRoute(id)
  const group = WORKSPACE_NAV.find((d) => d.key === "purchasing")?.groups?.find((g) => g.items.some(([r]) => r === route))
  const label = group?.items.find(([r]) => r === route)?.[1] || "Wireframes"
  crumb.innerHTML = `<a href="#start">Werkplek</a><span aria-hidden="true">/</span><a href="#dash">Productontwikkeling &amp; Inkoop</a><span aria-hidden="true">/</span><span>${esc(group?.label || "")}</span><span aria-hidden="true">/</span><a href="#${route}">${esc(label)}</a><span aria-hidden="true">/</span><span aria-current="page">${esc(id || "DA01")}</span>`
  document.title = `${label} · ${id || "DA01"} · VoyageVista`
}
const wfRedraw = redraw
redraw = function () {
  wfRedraw()
  if (parseHash().p === "wf") wfCrumb(parseHash().id)
}
