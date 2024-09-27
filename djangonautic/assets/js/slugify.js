const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug]");

const slugify = (val) => {
  const currentDateTime = new Date();
  const year = currentDateTime.getFullYear();
  const month = String(currentDateTime.getMonth() + 1).padStart(2, "0");
  const day = String(currentDateTime.getDate()).padStart(2, "0");
  const hours = String(currentDateTime.getHours()).padStart(2, "0");
  const minutes = String(currentDateTime.getMinutes()).padStart(2, "0");
  const seconds = String(currentDateTime.getSeconds()).padStart(2, "0");
  const timestamp = `${year}${month}${day}${hours}${minutes}${seconds}`;

  return (
    val
      .toString()
      .toLowerCase()
      .trim()
      .replace(/&/g, "-and-") // Replace & with 'and'
      .replace(/[\s\W-]+/g, "-") + // Replace spaces, non-word characters and dashes with a single dash (-)
    `-${timestamp}`
  ); // Append timestamp to ensure uniqueness
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.setAttribute("value", slugify(titleInput.value));
});
