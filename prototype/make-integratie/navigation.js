/* Single navigation tree: existing screens only; detail screens resolve to their parent. */
const WORKSPACE_NAV = [
  {
    key: "marketing",
    label: "Marketing & Communicatie",
    icon: "bulb",
    dashboardRoute: "marketingdash",
    items: [],
    routes: [],
  },
  {
    key: "sales",
    label: "Sales & Boekingen",
    icon: "brief",
    dashboardRoute: "salesdash",
    items: [],
    routes: ["cat", "catp", "fav", "meld", "saleswork", "salescustomer"],
  },
  {
    key: "service",
    label: "Klantenservice & Support",
    icon: "chat",
    dashboardRoute: "supportdash",
    items: [],
    routes: [
      ...NAV.ks[0][1].map((x) => x[0]).filter((x) => x !== "cat"),
      "klant",
      "zaak",
    ],
  },
  {
    key: "purchasing",
    label: "Productontwikkeling & Inkoop",
    icon: "box",
    dashboardRoute: "dash",
    items: [],
groups: [
  { key: "productontwikkeling", label: "Productontwikkeling", icon: "box",
    items: [["kansen","Productkansen"],["rps","Reisproducten"],["lijsten","Reisonderdelen & reisroutes"],["planning","Planning & voortgang"],["cat","Productcatalogus"],["wf.DA01","Nieuw · Dashboard"],["wf.PK01","Nieuw · Productkansen"],["wf.RP01","Nieuw · Reisproducten"],["wf.RD01","Nieuw · Reisonderdelen"],["wf.PL01","Nieuw · Planning"],["wf.CA01","Nieuw · Catalogus"],["wf.flows","Nieuw · Testflows user stories"]] },
  { key: "inkoop", label: "Inkoop", icon: "bld",
    items: [["levs","Leveranciers"],["aanbiedingen","Aanbiedingen"],["onds","Onderhandelingen"],["cts","Contracten"],["wf.LV01","Nieuw · Leveranciers"],["wf.AB01","Nieuw · Aanbiedingen"],["wf.ON01","Nieuw · Onderhandelingen"],["wf.CT01","Nieuw · Contracten"],["wf.AU01","Nieuw · Autorisatie"],["wf.index","Nieuw · Schermindex"]] },
],
  },
  {
    key: "finance",
    label: "Financiën & Administratie",
    icon: "coins",
    dashboardRoute: "financedash",
    items: [],
    routes: [],
  },
]
const SERVICE_ROUTES = new Set([
  ...NAV.ks[0][1].map((x) => x[0]).filter((x) => x !== "cat"),
  "klant",
  "zaak",
])
const PURCHASING_ROUTES = new Set([
  ...NAV.ink[0][1].map((x) => x[0]).filter((x) => x !== "cat"),
  "rp",
  "kans",
  "lev",
  "ond",
  "ct",
  "aanbiedingen",
  "wf",
])
function syncDepartmentRole(p) {
  if (SERVICE_ROUTES.has(p) && me().afd !== "ks") {
    S.role = "ks"
    save()
  }
  if (PURCHASING_ROUTES.has(p) && me().afd !== "ink") {
    S.role = "inkoper"
    save()
  }
}
allowed = (p) => !!PAGES[p]
U.navExpanded = {}
let navRoute = ""
let navRole = S.role
function navOwner(act) {
  if (act === "cat")
    return (
      (["purchasing", "sales"].includes(U.navDepartment)
        ? U.navDepartment
        : null) || (me().afd === "ink" ? "purchasing" : "sales")
    )
  return WORKSPACE_NAV.find(
    (d) =>
      d.dashboardRoute === act ||
      d.routes?.includes(act) ||
      d.items.some(([r]) => r === act) ||
      d.groups?.some((g) => g.items.some(([r]) => r === act)),
  )?.key
}
voyageNav = function (act) {
  if (navRole !== S.role) {
    U.navDepartment = undefined
    navRole = S.role
    navRoute = ""
  }
  const route = location.hash
  if (route !== navRoute) {
    const owner = navOwner(act)
    U.navDepartment = owner
    U.navExpanded = {}
    if (owner) U.navExpanded[owner] = true
    WORKSPACE_NAV.find((d) => d.key === owner)?.groups?.forEach((g) => {
      if (g.items.some(([r]) => r === act)) U.navExpanded[g.key] = true
    })
    navRoute = route
  }
  const link = ([r, l, role], dept) => {
    if (r === "kdash") l = serviceWorkspaceLabel()
    return `<a class="nav-sub-item" href="#${r}" title="${esc(l)}" data-a="workspacePage" data-d='${esc(JSON.stringify({ route: r, dept, role }))}' ${
      r === act && (!role || role === S.role) && dept === U.navDepartment
        ? 'aria-current="page"'
        : ""
    }><span>${esc(l)}</span></a>`
  }
  const group = (g, body, main = false) => {
    if (main) {
      const routeData = esc(
        JSON.stringify({ route: g.dashboardRoute, dept: g.key }),
      )
      const current =
        g.key === U.navDepartment
          ? 'aria-current="page"'
          : ""
      const toggle = body
        ? `<button class="department-toggle" type="button" data-a="navToggle" data-d='${esc(JSON.stringify({ key: g.key, main: true }))}' title="Menu ${esc(g.label)}" aria-label="Menu ${esc(g.label)}" aria-expanded="${!!U.navExpanded[g.key]}" aria-controls="nav-${g.key}">${ic("down", "nav-chevron " + (U.navExpanded[g.key] ? "open" : ""))}</button>`
        : ""
      const submenu = body
        ? `<div class="nav-sub ${U.navExpanded[g.key] ? "is-open" : ""}" id="nav-${g.key}">${body}</div>`
        : ""
      return `<div class="nav-accordion department-group"><div class="department-heading"><a class="department-main" href="#${g.dashboardRoute}" data-a="workspacePage" data-d='${routeData}' title="${esc(g.label)}" ${current}>${ic(g.icon)}<span>${esc(g.label)}</span></a>${toggle}</div>${submenu}</div>`
    }
    return `<div class="nav-accordion"><button class="nav-trigger" type="button" data-a="navToggle" data-d='${esc(JSON.stringify({ key: g.key, main: false }))}' title="${esc(g.label)}" aria-expanded="${!!U.navExpanded[g.key]}" aria-controls="nav-${g.key}">${ic(g.icon)}<span>${esc(g.label)}</span>${ic("down", "nav-chevron " + (U.navExpanded[g.key] ? "open" : ""))}</button><div class="nav-sub ${
      U.navExpanded[g.key] ? "is-open" : ""
    }" id="nav-${g.key}">${body}</div></div>`
  }
  return (
    `<div class="nav-label">Algemeen</div><a href="#start" title="Hoofddashboard" ${
      act === "start" ? 'aria-current="page"' : ""
    }>${ic("home")}<span>Hoofddashboard</span></a><div class="nav-divider"></div><div class="nav-label">Afdelingen</div>` +
    WORKSPACE_NAV.map((d) => {
      const body =
        d.items
          .filter(([route]) => !(S.role === "after" && route === "wv"))
          .map((x) => link(x, d.key))
          .join("") +
          (d.groups || [])
            .map((g) => group(g, g.items.map((x) => link(x, d.key)).join("")))
            .join("") +
        (!d.dashboardRoute && !d.items.length
          ? '<p class="nav-unavailable">Nog niet beschikbaar</p>'
          : "")
      return group(d, body, true)
    }).join("")
  )
}
A.navToggle = (el, ev, { key, main }) => {
  U.keepNavOpen = document.querySelector(".app").classList.contains("nav-open")
  const next = !U.navExpanded[key]
  if (main)
    WORKSPACE_NAV.forEach((d) => {
      if (d.key !== key) U.navExpanded[d.key] = false
    })
  if (!main)
    WORKSPACE_NAV.flatMap((d) => d.groups || []).forEach((g) => {
      if (g.key !== key) U.navExpanded[g.key] = false
    })
  U.navExpanded[key] = next
  redraw()
}
A.workspacePage = (el, ev, { route, dept, role }) => {
  ev.preventDefault()
  U.navDepartment = dept
  if (role) {
    S.role = role
    save()
  } else if (dept === "sales" && me().afd !== "cat") {
    S.role = "sales"
    save()
  }
  go(route)
}
A.deptInkoop = () => {
  syncDepartmentRole("dash")
  go("dash")
}
A.deptProductPage = (el, ev, { route }) => {
  ev.preventDefault()
  U.navDepartment = "purchasing"
  syncDepartmentRole(route)
  go(route)
}
function syncSidebarAccessibility() {
  const open = document.querySelector(".app").classList.contains("nav-open")
  document.querySelector(".side").inert =
    matchMedia("(max-width:860px)").matches && !open
  document
    .querySelector(".menu-btn")
    .setAttribute("aria-label", open ? "Menu sluiten" : "Menu openen")
}
const renderWorkspace = redraw
redraw = function () {
  renderWorkspace()
  syncSidebarAccessibility()
}
document.addEventListener("click", syncSidebarAccessibility)
window.addEventListener("resize", syncSidebarAccessibility)
document.addEventListener("keydown", (ev) => {
  if (ev.key === "Escape" && matchMedia("(max-width:860px)").matches) {
    syncSidebarAccessibility()
    if (document.activeElement?.closest(".side"))
      document.querySelector(".menu-btn").focus()
  }
})
document.addEventListener("keydown", (ev) => {
  if (
    !matchMedia("(max-width:860px)").matches ||
    !document.querySelector(".app.nav-open")
  )
    return
  if (ev.key === "Tab") {
    const nodes = [
      ...document.querySelectorAll(".side a,.side button,.menu-btn"),
    ].filter(
      (e) => e.getClientRects().length && !e.closest(".nav-sub:not(.is-open)"),
    )
    if (ev.shiftKey && document.activeElement === nodes[0]) {
      ev.preventDefault()
      nodes.at(-1).focus()
    } else if (!ev.shiftKey && document.activeElement === nodes.at(-1)) {
      ev.preventDefault()
      nodes[0].focus()
    }
  }
})
