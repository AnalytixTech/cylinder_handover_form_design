import reflex as rx
from cylinder_handover_form_design.states.auth_state import AuthState
from cylinder_handover_form_design.states.cylinder_state import CylinderState
from cylinder_handover_form_design.pages.sign_in_page import sign_in_page
from cylinder_handover_form_design.pages.handover_entry_page_1 import (
    handover_entry_page_1,
)
from cylinder_handover_form_design.pages.handover_entry_page_2 import (
    handover_entry_page_2,
)
from cylinder_handover_form_design.pages.submissions_page import submissions_page

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(sign_in_page, route="/sign-in")
app.add_page(sign_in_page, route="/")
app.add_page(
    handover_entry_page_1,
    route="/handover_entry_p1",
    on_load=AuthState.check_session,
)
app.add_page(
    handover_entry_page_2,
    route="/handover_entry_p2",
    on_load=AuthState.check_session,
)
app.add_page(
    submissions_page,
    route="/submissions",
    on_load=[
        AuthState.check_session,
        CylinderState.fetch_db_submissions,
    ],
)