const API_BASE = import.meta.env.VITE_API_BASE_URL;

export async function fetchCourses() {
  const res = await fetch(`/api/courses/`);
  if (!res.ok) {
    throw new Error("Failed to fetch courses");
  }
  const data = await res.json();

  // Support both paginated (with `results`) and plain list responses
  return Array.isArray(data) ? data : data.results;
}

export async function fetchCourseBySlug(slug: string) {
  const res = await fetch(`/api/courses/${slug}/`);
  if (!res.ok) {
    throw new Error("Course not found");
  }
  return res.json();
}
