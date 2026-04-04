import API from "@/lib/api";

export type SessionUser = {
  user_id: number;
  role: string;
};

export async function getCurrentUser(): Promise<SessionUser | null> {
  try {
    const res = await API.get("/api/me/");
    return res.data as SessionUser;
  } catch {
    return null;
  }
}

export async function logout(): Promise<void> {
  await API.post("/api/auth/logout");
}
