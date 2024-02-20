export default function AuthButton({ name }) {
  return (
    <button type="submit" classNameName="btn btn-primary w-100 auth-btn">
      {name}
    </button>
  );
}
