from django.shortcuts import render

# Create your views here.

def smartphone(request):
    filtros = {
        "Marca": ["Samsung", "Apple", "Xiaomi", "Honor"],
        "modelo": ["Galaxy S23", "iPhone 14", "Redmi Note 12", "Honor Magic 5"],
        "sistema operativo": ["Android", "iOS"],
        "pantalla": ["5.5 a 6.0 pulgadas", "6.1 a 6.5 pulgadas", "6.6 pulgadas o más"],
        "almacenamiento": ["64 GB", "128 GB", "256 GB"],
        "bateria": ["4000 mAh", "5000 mAh", "6000 mAh"],
        "camara": ["12 MP", "48 MP", "108 MP"]
    }
    return render(request, "app_productos/smartphone.html", {
        "tipo_submenu": "filtros",
        "categoria": "smartphone",
        "filtros": filtros
    })


def notebook(request):
    filtros = {
    "marca": ["HP", "Dell", "Lenovo", "Apple"],
    "modelo": ["MacBook Air M2", "Dell XPS 13", "HP Pavilion", "Lenovo ThinkPad"],
    "procesador": ["Intel i5", "Intel i7", "AMD Ryzen 5", "Apple M2"],
    "ram": ["8 GB", "16 GB", "32 GB"],
    "almacenamiento": ["256 GB SSD", "512 GB SSD", "1 TB SSD"],
    "pantalla": ["13.3 pulgadas", "14 pulgadas", "15.6 pulgadas"],
    "sistema_operativo": ["Windows 11", "macOS", "Linux"]
}
    return render(request, "app_productos/notebook.html", {
        "tipo_submenu": "filtros",
        "categoria": "notebook",
        "filtros": filtros
    })

def tablet(request):
    filtros = {
    "marca": ["Samsung", "Apple", "Huawei", "Lenovo"],
    "modelo": ["iPad 10ª gen", "Galaxy Tab S9", "Huawei MatePad", "Lenovo Tab M10"],
    "pantalla": ["8 pulgadas", "10.1 pulgadas", "12.9 pulgadas"],
    "almacenamiento": ["64 GB", "128 GB", "256 GB"],
    "sistema_operativo": ["Android", "iPadOS"],
    "conectividad": ["Wi-Fi", "Wi-Fi + LTE"]
}

    return render(request, "app_productos/tablet.html", {
        "tipo_submenu": "filtros",
        "categoria": "tablet",
        "filtros": filtros
    })

def pc_escritorio(request):
    filtros = {
    "marca": ["HP", "Dell", "Lenovo", "Asus"],
    "procesador": ["Intel i5", "Intel i7", "AMD Ryzen 5", "AMD Ryzen 7"],
    "ram": ["8 GB", "16 GB", "32 GB"],
    "almacenamiento": ["1 TB HDD", "512 GB SSD", "1 TB SSD"],
    "sistema_operativo": ["Windows 11", "Linux"],
    "tipo": ["Torre", "All-in-One"]
}

    return render(request, "app_productos/pc_escritorio.html",{
        "tipo_submenu": "filtros",
        "categoria": "pc escritorio",
        "filtros": filtros
    })

def televisor(request):
    filtros = {
    "marca": ["Samsung", "LG", "Sony", "TCL"],
    "tipo": ["Smart TV", "LED", "OLED", "QLED"],
    "tamaño": ["32 pulgadas", "43 pulgadas", "55 pulgadas", "65 pulgadas"],
    "resolución": ["HD", "Full HD", "4K UHD", "8K"],
    "sistema_operativo": ["Tizen", "webOS", "Android TV", "Roku TV"],
    "conectividad": ["Wi-Fi", "Bluetooth", "Ethernet"]
}

    return render(request, "app_productos/televisor.html",{
        "tipo_submenu": "filtros",
        "categoria": "televisores",
        "filtros": filtros
    })