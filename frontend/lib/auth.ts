import API from "@/lib/api";

export type SessionUser = {
  user_id: number;
  name: string;
  role: string;
};

export async function getCurrentUser(): Promise<SessionUser | null> {
  try {
    const res = await API.get("/api/me/");
    const raw = res.data as {
      user_id?: number;
      name?: string;
      user_name?: string;
      role?: string;
    };

    if (!raw.user_id || !raw.role) {
      return null;
    }

    return {
      user_id: raw.user_id,
      name: raw.name ?? raw.user_name ?? "User",
      role: raw.role,
    };
  } catch {
    return null;
  }
}

export async function logout(): Promise<void> {
  await API.post("/api/auth/logout");
}
