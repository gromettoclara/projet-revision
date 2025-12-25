function review(choice, sic) {
    XsltForms_xmlevents.dispatch(
        document.getElementById("review"),
        "callbackevent",
        null,
        null,
        null,
        null,
        {
            choice: choice,
            sic: sic
        }
    );
}
console.log("reviewer() est chagée")
