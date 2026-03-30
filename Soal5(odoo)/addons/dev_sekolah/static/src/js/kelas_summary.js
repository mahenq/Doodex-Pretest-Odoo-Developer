/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class KelasSummaryOWL extends Component {
    setup() {
        this.record = this.props.record.data;
    }
}

KelasSummaryOWL.template = "dev_sekolah.KelasSummaryOWL";

registry.category("fields").add("kelas_summary_owl", {
    component: KelasSummaryOWL,
});