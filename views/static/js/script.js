var exterior = document.getElementById("Exterior");
var interior = document.getElementById("Interior");
var summary = document.getElementById("Summary");
var part0 = document.getElementById("part0");
var part1 = document.getElementById("part1");
var btn = document.getElementById("buyBtn");

window.localStorage.setItem('idCar', (new URLSearchParams(window.location.search)).get("id"))
// window.localStorage.setItem('curType', 'Exterior')
// window.localStorage.setItem('curSubtype', 'Color')

const handleChangeTab = () => {
    subtype = window.localStorage.getItem('curSubtype');
    if (subtype == "Summary") rerurn; 
    value = Array.from(document.getElementsByName(subtype)).find(e => e.checked)
    if (value == undefined) return;
    else value = value.value
    form = window.localStorage.getItem('form')
    if (form == undefined){
        window.localStorage.setItem('form', {subtype: value})
    } 
    else{
        form[subtype] = value
        window.localStorage.setItem('form', form)
    }
}

exterior.addEventListener('click', () => {
    handleChangeTab()
    window.localStorage.setItem('curType', 'Exterior')
    window.localStorage.setItem('curSubtype', 'Color')
    car = window.localStorage.getItem('idCar')
    window.location.href = `/customer/build?id=${car}&type=Exterior&subtype=Color`
})
interior.addEventListener('click', () => {
    handleChangeTab()
    window.localStorage.setItem('curType', 'Interior')
    window.localStorage.setItem('curSubtype', 'U')
    car = window.localStorage.getItem('idCar')
    window.location.href = `/customer/build?id=${car}&type=Interior&subtype=Upholstery`
})
summary.addEventListener('click', () => {
    handleChangeTab()
    window.localStorage.setItem('curType', 'Summary')
    car = window.localStorage.getItem('idCar')
    form = window.localStorage.getItem('form')
    query = ""
    if (form != undefined)
        for (const key of Object.keys(form)) {
            query = query + `&${key}=${form[key]}`
        }
    window.location.href = `/customer/build?id=${car}&type=Summary&subtype=${query}`
})
if (part0 != undefined)
    part0.addEventListener('click', () => {
        handleChangeTab()
        type = window.localStorage.getItem('curType')
        subtype = part0.innerHTML
        car = window.localStorage.getItem('idCar')
        window.localStorage.setItem('curSubtype', subtype)
        window.location.href = `/customer/build?id=${car}&type=${type}&subtype=${subtype}`
    });
if (part1 != undefined)
    part1.addEventListener('click', () => {
        handleChangeTab()
        type = window.localStorage.getItem('curType')
        subtype = part1.innerHTML
        car = window.localStorage.getItem('idCar')
        window.localStorage.setItem('curSubtype', subtype)
        window.location.href = `/customer/build?id=${car}&type=${type}&subtype=${subtype}`
    });

if (btn != undefined)
    btn.addEventListener('click', async () => {
        data = window.localStorage.getItem('form')
        if (data == undefined) data = {};
        data['carID'] = window.localStorage.getItem('idCar')
        var res = await fetch('/customer/build', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        console.log(res)
        alert('Complete')
        window.localStorage.clear()
        window.location.href = '/customer'
    })
