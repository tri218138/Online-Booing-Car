var exterior = document.getElementById("Exterior");
var interior = document.getElementById("Interior");
var summary = document.getElementById("Summary");
var part0 = document.getElementById("part0");
var part1 = document.getElementById("part1");
var btn = document.getElementById("buyBtn");
//window.localStorage.clear()
window.localStorage.setItem('idCar', (new URLSearchParams(window.location.search)).get("id"))
if (window.localStorage.getItem('curType') == undefined)
    window.localStorage.setItem('curType', 'Exterior')
if (window.localStorage.getItem('curSubtype') == undefined)
    window.localStorage.setItem('curSubtype', 'Color')
// window.localStorage.setItem('curSubtype', 'Color')
form = JSON.parse(window.localStorage.getItem('form'))
console.log(form, window.localStorage.getItem('curSubtype'))
const handleChangeTab = () => {
    subtype = window.localStorage.getItem('curSubtype');
    if (subtype == "Summary") rerurn; 
    value = document.querySelector(`input[name=${subtype}]:checked`);
    if (value == undefined) return;
    else value = value.value
    form = JSON.parse( window.localStorage.getItem('form'))
    if (form == undefined){
        form = {}
        form[subtype] = value
        window.localStorage.setItem('form', JSON.stringify(form))
    } 
    else{
        form[subtype] = value
        window.localStorage.setItem('form', JSON.stringify(form))
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
    window.localStorage.setItem('curSubtype', 'Upholstery')
    car = window.localStorage.getItem('idCar')
    window.location.href = `/customer/build?id=${car}&type=Interior&subtype=Upholstery`
})
summary.addEventListener('click', () => {
    handleChangeTab()
    window.localStorage.setItem('curType', 'Summary')
    car = window.localStorage.getItem('idCar')
    form = JSON.parse(window.localStorage.getItem('form'))
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
        data = JSON.parse(window.localStorage.getItem('form'))
        if (data == undefined) data = {};
        data['carID'] = window.localStorage.getItem('idCar')
        console.log(data)
        var res = await fetch('/customer/build', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        res = await res
        console.log(res)
        alert('BMW cảm ơn bạn đã đồng hành')
        window.localStorage.clear()
        window.location.href = '/customer'
    })
