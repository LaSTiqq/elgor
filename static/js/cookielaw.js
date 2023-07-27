var Cookielaw = {
  ACCEPTED: "1",
  REJECTED: "0",

  createCookie: function (name, value, days) {
    var date = new Date(),
      expires = "";
    if (days) {
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toGMTString();
    } else {
      expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
  },

  createCookielawCookie: function (cookieValue, secure = true) {
    const cookie = document.getElementById("CookielawBanner");
    cookieValue = cookieValue || this.ACCEPTED;
    this.createCookie("cookielaw_accepted", cookieValue, 10 * 365, secure);
    cookie.style.visibility = "hidden";
    cookie.style.opacity = "0";
  },

  accept: function () {
    this.createCookielawCookie(this.ACCEPTED);
  },

  reject: function () {
    this.createCookielawCookie(this.REJECTED);
  },
};
