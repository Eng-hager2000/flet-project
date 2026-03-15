import flet as ft 

def main(page: ft.Page):
    page.title = "تسجيل المنصرف"
    page.rtl = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"   # يسمح بالتمرير عند زيادة البيانات
    total = 0
    amount = ft.TextField(label="المبلغ", width=150, text_align="right")
    details = ft.TextField(label="التفاصيل", width=300, text_align="right")

    total_text = ft.Text("الإجمالي: 0", size=22, weight="bold")

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("المبلغ")),
            ft.DataColumn(ft.Text("التفاصيل")),
        ],
        rows=[]  
    )

    def add_record(e):
        nonlocal total

        if amount.value:
            value = float(amount.value)
            total += value

            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(amount.value)),
                        ft.DataCell(ft.Text(details.value)),
                    ]
                )
            )

            total_text.value = f"الإجمالي: {total}"

            amount.value = ""
            details.value = ""

            page.update()

    page.add(
        ft.Container(
            width=600,
            padding=20,
            content=ft.Column(
                controls=[

                    ft.Text(
                        "تسجيل المنصرف",
                        size=28,
                        weight="bold"
                    ),

                    ft.Row(
                        [
                            amount,
                            details,
                            ft.ElevatedButton(
                                "إضافة",
                                icon=ft.Icons.ADD,
                                on_click=add_record
                            )
                        ]
                    ),

                    ft.Divider(),

                    ft.Row(
                        [total_text],
                        alignment=ft.MainAxisAlignment.END
                    ),

                    table,
                ]
            )
        )
    )

ft.app(target=main)
